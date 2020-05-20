from django.urls import path
from work import views

urlpatterns = [
    path('jobs', views.JobList.as_view()),
    path('jobs/<uuid:job_id>', views.JobDetail.as_view()),
]
