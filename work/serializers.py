from rest_framework import serializers
from work.models import Job


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Job

    start_month = serializers.SerializerMethodField()
    end_month = serializers.SerializerMethodField()

    def get_start_month(self, obj):
        return obj.get_start_month_display()

    def get_end_month(self, obj):
        return obj.get_end_month_display()
