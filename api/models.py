from django.db import models
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.dispatch import receiver
from django.db.models.signals import post_save

class BucketList(models.Model):
  """BucketList model Class"""

  name = models.CharField(max_length=255, blank=False, unique=True)
  owner = models.ForeignKey('auth.User',
  related_name='bucket_list',
  on_delete=models.CASCADE)
  date_created = models.DateTimeField(auto_now_add=True)
  date_modified = models.DateTimeField(auto_now=True)

  def __str__(self):
    """Human Readable"""
    return '{}'.format(self.name)

@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
  if created:
    Token.objects.create(user=instance)