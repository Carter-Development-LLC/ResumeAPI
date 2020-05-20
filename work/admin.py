from django.contrib import admin
from work.models import Job

class JobAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'start_month', 'start_year', 'end_month', 'end_year']

admin.site.register(Job, JobAdmin)
