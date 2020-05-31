from rest_framework.views import APIView
from rest_framework.response import Response
from about.models import Bio
from about.serializers import BioSerializer


class BioDetail(APIView):
    def get(self, request):
        serializer = BioSerializer(Bio.objects.latest('content'))
        return Response(serializer.data)
