from django.contrib import admin
from django.utils.html import format_html
from .models import Course, Tag, Learning, Prerequisite, Video, UserCourse, Payment, CouponCode, Contact
from import_export import resources
from import_export.admin import ImportExportModelAdmin, ImportExportMixin

class TagInline(admin.TabularInline):
    model = Tag

class PrerequisiteInline(admin.TabularInline):
    model = Prerequisite

class LearningInline(admin.TabularInline):
    model = Learning

class VideoInline(admin.TabularInline):
    model = Video

class CourseResource(resources.ModelResource):
    class Meta:
        model = Course

@admin.register(Course)
class CourseAdmin(ImportExportMixin, admin.ModelAdmin):
    inlines = [TagInline, LearningInline, PrerequisiteInline, VideoInline]
    list_display = ['name', 'get_price', 'get_discount', 'active', 'view']
    list_filter = ['active', 'discount']


    def get_price(self, course):
        return f'\u20B9 {course.price}'

    def get_discount(self, course):
        return f'{course.discount} %'

    def view(self, course):
        return format_html(f'<a target="_blank" href="/course/{course.slug}">Live Preview</a>')

    get_price.short_description = 'price'
    get_discount.short_description = 'discount'

    
class VideoAdmin(admin.ModelAdmin):
    list_display = ['get_course', 'title', 'is_preview']
    list_filter = ['is_preview', 'course']

    def get_course(self, video):
        return format_html(f'<a target="_blank" href="/admin/courses/course/{video.course.id}">{video.course}</a>')

    get_course.short_description = 'course'


class PaymentAdmin(admin.ModelAdmin):
    list_display = ['order_id', 'get_user', 'get_course', 'status']
    list_filter = ['status', 'course']

    def get_user(self, payment):
        return format_html(f'<a target="_blank" href="/admin/auth/user/{payment.user.id}">{payment.user}</a>')

    def get_course(self, payment):
        return format_html(f'<a target="_blank" href="/admin/courses/course/{payment.course.id}">{payment.course}</a>')

    get_user.short_description = 'user'
    get_course.short_description = 'course'



class UserCourseAdmin(admin.ModelAdmin):
    list_display = ['get_usercourse', 'get_user', 'get_course']
    list_filter = ['course']

    def get_usercourse(self, usercourse):
        return 'UserCourse'

    def get_user(self, usercourse):
        return format_html(f'<a target="_blank" href="/admin/auth/user/{usercourse.user.id}">{usercourse.user}</a>')

    def get_course(self, usercourse):
        return format_html(f'<a target="_blank" href="/admin/courses/course/{usercourse.course.id}">{usercourse.course}</a>')

    get_course.short_description = 'course'
    get_user.short_description = 'user'
    get_usercourse.short_description = 'usercourse'



admin.site.register(Video, VideoAdmin)
admin.site.register(UserCourse, UserCourseAdmin)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(CouponCode)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('email', 'date')

