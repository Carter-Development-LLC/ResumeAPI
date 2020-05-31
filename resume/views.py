from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request):
    return Response({
        'about': reverse('bio-detail', request=request),
        'education': reverse('schools-list', request=request),
        'work': reverse('jobs-list', request=request),
    })
