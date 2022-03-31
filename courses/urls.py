from django.urls import path
from .views import (
	HomeListView, courseDetail, ContactView, CourseListView, 
	checkout, verifyPayment, MyCoursesList, AboutView, SearchResultsView
)

urlpatterns = [
	path('', HomeListView.as_view(), name='home'),
	path('about', AboutView.as_view(), name='about'),
	path('courses/', CourseListView.as_view(), name='courses'),
	path('contact/', ContactView.as_view(), name='contact'),
	path('search/', SearchResultsView.as_view(), name='search_results'),

	path('course/<slug:slug>/', courseDetail, name='courseDetail'),
	path('checkout/<slug:slug>/', checkout, name='checkout'),
	path('verify_payment/', verifyPayment, name='verify_payment'),
	path('my_courses/', MyCoursesList.as_view(), name='my_courses'),
]