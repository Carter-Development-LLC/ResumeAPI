from django.urls import path
from about import views

urlpatterns = [
    path('bio', views.BioDetail.as_view(), name='bio-detail')
]
