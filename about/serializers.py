from rest_framework import serializers
from about.models import Bio


class BioSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Bio
