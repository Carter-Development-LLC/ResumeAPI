from django.urls import path
from education import views

urlpatterns = [
    path('schools', views.SchoolList.as_view()),
    path('schools/<uuid:school_id>', views.SchoolDetail.as_view()),
    path('schools/<uuid:school_id>/courses', views.CourseList.as_view()),
    path('schools/<uuid:school_id>/courses/<uuid:course_id>', views.CourseDetail.as_view()),
]
