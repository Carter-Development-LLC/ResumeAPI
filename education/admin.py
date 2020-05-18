from django.contrib import admin
from education.models import Course, School

class CourseAdmin(admin.ModelAdmin):
    list_display = ['stub', 'semester', 'year', 'featured']
    list_filter = ['featured']

admin.site.register(Course, CourseAdmin)
admin.site.register(School)
