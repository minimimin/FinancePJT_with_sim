from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Profile
from .serializers import ProfileSerializer

# Create your views here.
@api_view(['GET', 'POST', 'PUT'])
@permission_classes([IsAuthenticated])
def user_profile(request, user_pk):
    if request.method == 'GET':
        profile = Profile.objects.get(user_id=user_pk)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    elif request.method == 'PUT':
        profile = Profile.objects.get(user_id=user_pk)
        serializer = ProfileSerializer(profile, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)