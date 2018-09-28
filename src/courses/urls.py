from django.urls import path
from .views import(
     courseView,
     courseListView,
	)

app_name="courses"
urlpatterns = [
    #path('',CourseView.as_view(template_name="social.html"),name="course_list"),
    path('course/<int:id>/',courseView.as_view(),name="course_detail"),
    path('course/',courseListView.as_view(),name="course_list"),
]    