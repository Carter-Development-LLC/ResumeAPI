from rest_framework import serializers
from education.models import Course, School

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = School

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Course

    semester = serializers.SerializerMethodField()

    def get_semester(self, obj):
        return obj.get_semester_display()
