# api/serializers.py

from rest_framework import serializers
from .models import BucketList

class BucketListSerializer(serializers.ModelSerializer):
  """Serialize Models to JSON"""

  owner = serializers.ReadOnlyField(source='owner.username')

  class Meta:
    """Meta class mapping model fields to serializer fields"""

    model = BucketList

    fields = ('id', 'name', 'owner','date_created', 'date_modified')
    read_only_fields = ('date_created', 'date_modified')