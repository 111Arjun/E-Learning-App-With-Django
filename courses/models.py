from django.db import models
from django.contrib.auth.models import User

# Create your models here.

COURSE_LEVEL = (
    ('Beginner', 'Beginner', ),
    ('Intermediate', 'Intermediate'),
    ('Advanced', 'Advanced')
)

class Course(models.Model):
    name = models.CharField(max_length=100, null=False)
    slug = models.SlugField(max_length=100, null=False, unique=True)
    description = models.TextField(null=True)
    price = models.IntegerField(null=False)
    discount = models.IntegerField(null=False, default=0)
    created = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField(upload_to='files/thumnail')
    resource = models.FileField(upload_to='files/resource', blank=True, null=True)
    length = models.IntegerField(null=False)
    active = models.BooleanField(default=False, null=True)
    level = models.CharField(choices=COURSE_LEVEL, default='Beginner', max_length=15)


    def __str__(self):
        return self.name
    

class CourseProperty(models.Model):
    course = models.ForeignKey(Course, null=False, on_delete=models.CASCADE)
    description = models.CharField(null=False, max_length=70)

    def __str__(self):
        return self.description

    class Meta:
        abstract = True   


class Tag(CourseProperty):
    pass

class Prerequisite(CourseProperty):
    pass

class Learning(CourseProperty):
    pass


class Video(models.Model):
    course = models.ForeignKey(Course, null=False, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=False)
    serial_number = models.IntegerField(null=False)
    video_id = models.CharField(max_length=100, null=False)
    is_preview = models.BooleanField(default=False)


    def __str__(self):
        return self.title
    
# The following model is for particular user
# Like Who is the user and getting all the user details as his enrolled course and date
class UserCourse(models.Model):
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, null=False, on_delete=models.CASCADE)
    enroll_date = models.DateTimeField(auto_now_add=True)


    class Meta:
        pass

    def __str__(self):
        return f'{self.user.username} - {self.course}'



class Payment(models.Model):
    order_id = models.CharField(max_length=100, null=False)  # when you enrolled in course, null=False because wheb you enrolled in course we want that id which is order_id
    payment_id = models.CharField(max_length=100)  # It will be added once payment  is successfull, if payment fails then it will be null
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, null=False, on_delete=models.CASCADE)
    user_course = models.ForeignKey(UserCourse, null=True, blank=True,on_delete=models.CASCADE)  # When Payment is successfull there will be no userCouse
    created = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)




class CouponCode(models.Model):
    code = models.CharField(max_length=6)
    course = models.ForeignKey(Course, null=False, on_delete=models.CASCADE, related_name='coupons')
    discount = models.IntegerField(default=0)


    def __str__(self):
        return f'{self.course} - {self.code}'
    

class Contact(models.Model):        
    date = models.DateTimeField(auto_now_add=True)
    subject = models.CharField(verbose_name="Subject",max_length=250)
    email = models.EmailField(verbose_name="Email")
    message = models.TextField(verbose_name="Message")

    def __str__(self):
        return f'{self.email}'








