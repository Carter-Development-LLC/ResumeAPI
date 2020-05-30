from rest_framework.generics import ListAPIView, RetrieveAPIView
from work.models import Job
from work.serializers import JobSerializer


class JobList(ListAPIView):
    queryset = Job.objects.all().order_by(
        '-currently_employed', '-end_year', '-end_month')
    serializer_class = JobSerializer


class JobDetail(RetrieveAPIView):
    queryset = Job.objects
    serializer_class = JobSerializer
    lookup_url_kwarg = 'job_id'
