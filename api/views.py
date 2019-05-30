from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework import permissions

from .serializers import BucketListSerializer
from .models import BucketList
from .permissions import IsOwner

# ListCreateAPIView is a generic view which provides GET (list all) and POST method handlers
# IsAuthenticatedOrReadOnly which permits unauthenticated users if the request is one of the "safe" methods (GET, HEAD and OPTIONS)
class BucketListCreateView(ListCreateAPIView):
  """View responsible for creating bucketlist items"""

  queryset = BucketList.objects.all()
  serializer_class = BucketListSerializer
  permission_class = (permissions.IsAuthenticated, IsOwner)

  def create_bucketlist_item(self, serializer):
    """Save POST data"""
    serializer.save(owner=self.request.user)

# RetrieveUpdateDestroyAPIView is a generic view that provides GET(one), PUT, PATCH and DELETE method handlers.
class DetailsView(RetrieveUpdateDestroyAPIView):
  """View responsible for Read, Update and Delete"""

  queryset = BucketList.objects.all()
  serializer_class = BucketListSerializer
  permission_class = (permissions.IsAuthenticated, IsOwner)