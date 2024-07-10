from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions

from django.http import JsonResponse
from cves.models import CVE
from cves.serializers import CVESerializer


# Create your views here.
@api_view(["GET"])
@permission_classes([permissions.AllowAny])
def cves(request):

    cves = CVE.objects.all()
    serializer = CVESerializer(cves, many=True)
    return JsonResponse(serializer.data, safe=False)
