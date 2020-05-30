from django.urls import path
from education import views

urlpatterns = [
    path('schools', views.SchoolList.as_view(), name='schools-list'),
    path('schools/<uuid:school_id>',
         views.SchoolDetail.as_view(), name='school-detail'),
    path('schools/<uuid:school_id>/courses',
         views.CourseList.as_view(), name='courses-list'),
    path('schools/<uuid:school_id>/courses/<uuid:course_id>',
         views.CourseDetail.as_view(), name='course-detail'),
]
