from rest_framework.permissions import BasePermission
from .models import BucketList

class IsOwner(BasePermission):
  """Custom class, gives bucketlist owners edit privs"""

  def has_perm(self, req, view, obj):
    if isinstance(obj, BucketList):
      return obj.owner == req.owner
    return obj.owner == request.user