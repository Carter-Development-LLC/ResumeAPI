from rest_framework.generics import ListAPIView, RetrieveAPIView
from education.models import Course, School
from education.serializers import CourseSerializer, SchoolSerializer


class SchoolList(ListAPIView):
    queryset = School.objects.all().order_by('name')
    serializer_class = SchoolSerializer


class SchoolDetail(RetrieveAPIView):
    queryset = School.objects
    serializer_class = SchoolSerializer
    lookup_url_kwarg = 'school_id'


class CourseList(ListAPIView):
    queryset = Course.objects.all().order_by('-year', 'semester', 'stub')
    serializer_class = CourseSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        school_id = self.kwargs['school_id']
        featured = self.request.query_params.get('featured', False) == 'true'

        if featured:
            queryset = queryset.filter(featured=True)

        return queryset.filter(school_id=school_id)


class CourseDetail(RetrieveAPIView):
    queryset = Course.objects
    serializer_class = CourseSerializer
    lookup_url_kwarg = 'course_id'
