from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.conf import settings
from django.db.models import Q
from allauth.account.decorators import login_required

from .models import Course, Video, Payment, UserCourse, CouponCode
from .forms import ContactForm

import razorpay
client = razorpay.Client(auth=(settings.KEY_ID, settings.KEY_SECRET))
 

class HomeListView(generic.ListView):
    template_name = 'courses/home.html'
    queryset = Course.objects.filter(active=True)

class SearchResultsView(generic.ListView):
    model = Course
    template_name = 'courses/search.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Course.objects.filter(
            Q(name__icontains=query)
        )
        return object_list

class AboutView(generic.TemplateView):
    template_name = 'courses/about.html'

class CourseListView(generic.ListView):
    template_name = 'courses/courses.html'
    paginate_by = 4
    queryset = Course.objects.filter(active=True)
    

def courseDetail(request, slug):
    course = Course.objects.get(slug=slug)
    serial_number = request.GET.get('lecture')  # lecture is the key from the url
    videos = course.video_set.all().order_by('serial_number')
    next_lecture = 2     # Setting the initial value at 2
    previous_lecture = None

    if serial_number is None:
        serial_number = 1
    else:
        next_lecture = int(serial_number) + 1
        if len(videos) < next_lecture:
            next_lecture = None

        previous_lecture = int(serial_number) - 1

    video = Video.objects.get(serial_number=serial_number, course=course) # This will get the particular object of the video we want to serve

    if video.is_preview is False:
        if request.user.is_authenticated is False:
            return redirect('account_login')
        else:
            user = request.user
            try:
                user_course = UserCourse.objects.get(user = user, course = course)
            except:
                return redirect('checkout', slug=course.slug)
    
    context = {
        'course': course,
        'video':video,
        'videos':videos,
        'next_lecture':next_lecture,
        'previous_lecture':previous_lecture
    }
    return render(request, 'courses/courseDetail.html', context)



@login_required
def checkout(request, slug):
    course = Course.objects.get(slug=slug)
    user = request.user

    action = request.GET.get('action')  # action is key from url when user proceeds to payment
    couponcode = request.GET.get('couponcode') 
    couponcode_message = None
    coupon = None
    order = None
    payment = None
    error = None
    amount = None

    try:
        user_course = UserCourse.objects.get(user = user, course = course)
        error = 'You are already Enrolled in the Course'

        if error:
            return redirect('my_courses')
    except:
        pass

    if error is None :
        amount = int((course.price - ( course.price * course.discount * 0.01 )) * 100)

    if couponcode:
        print('couponcode', couponcode)
        try:
            coupon = CouponCode.objects.get(course=course, code=couponcode)
            amount = int((course.price - ( course.price * coupon.discount * 0.01 )) * 100)
            print('amount', amount)
        except:
            couponcode_message = 'Invalid Coupon Code'

    if amount == 0:
        user_course = UserCourse(user = user, course = course)
        user_course.save()
        messages.success(request, 'You are successfully enrolled in the course')
        return redirect('my_courses')



    if action == 'create_payment':
        
            DATA = {
                "amount" : amount,
                "currency" : 'NPR',
                "notes" : {
                    "email":user.email,
                    "name": f'{user.first_name} {user.last_name}',
                }
            }

            order = client.order.create(data=DATA)

            payment = Payment()
            payment.user = user
            payment.course = course
            payment.order_id = order.get('id')
            payment.save()

    

    context = {
        'course': course,
        'order':order,
        'payment':payment,
        'user':user,
        'error':error,
        'couponcode_message':couponcode_message,
        'coupon':coupon,
        'Razorpay_KEY_ID': settings.KEY_ID,
        'DOMAIN_URL': settings.DOMAIN_URL
    }
    return render(request, 'courses/checkout.html', context)


@csrf_exempt
def verifyPayment(request):
    if request.method == 'POST':
        data = request.POST
        try:
            client.utility.verify_payment_signature(data)
            razorpay_order_id = data['razorpay_order_id']
            razorpay_payment_id = data['razorpay_payment_id']

            payment = Payment.objects.get(order_id = razorpay_order_id)
            payment.payment_id = razorpay_payment_id
            payment.status = True

            userCourse = UserCourse(user = payment.user, course = payment.course)
            userCourse.save()

            payment.user_course = userCourse
            payment.save()
            
            messages.success(request, 'You are successfully enrolled in the course')
            return redirect('my_courses')
        except:
            return HttpResponse('Invalid Payment Details')


@method_decorator(login_required, name='dispatch')
class MyCoursesList(generic.ListView):
    template_name = 'courses/my_courses.html'

    def get_queryset(self):
        return UserCourse.objects.filter(user = self.request.user)


class ContactView(generic.FormView):
    template_name = "courses/contact.html"
    form_class = ContactForm
    success_url = "/"
    
    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Thank you. We will be in touch soon.')
        return super().form_valid(form)
