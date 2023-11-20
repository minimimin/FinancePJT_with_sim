from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import RegionSerializer
from .models import Region

# Create your views here.
@api_view(['GET'])
def address_list(request):
    if request.method == 'GET':
        regions = Region.objects.all()
        serializer = RegionSerializer(regions, many=True)
        return Response(serializer.data)
