from django.urls import path
from work import views

urlpatterns = [
    path('jobs', views.JobList.as_view(), name='jobs-list'),
    path('jobs/<uuid:job_id>', views.JobDetail.as_view(), name='job-detail'),
]
