# api/tests.py

from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User

from .models import BucketList

class ModelTestCase(TestCase):
  """Test case for Bucketlist model"""

  def setUp(self):
    """Intial Setup, test client"""
    user = User.objects.create(username='testbucket')
    self.name = 'Test user'
    self.bucketlist = BucketList(name=self.name, owner=user)
  
  def test_model_can_create_bucketlist(self):
    """Test Bucketlist model"""
    old_count = BucketList.objects.count()
    self.bucketlist.save()
    new_count = BucketList.objects.count()
    self.assertNotEqual(old_count, new_count)

class ViewTestCase(TestCase):
  """Test suite for Bucketlist model"""

  def setUp(self):
    """API test client"""
    user = User.objects.create(username='testbucket')
    self.client = APIClient()
    self.client.force_authenticate(user=user)
    self.bucketlist_data = {'name': 'Build enterprise level software and web apps'}
    self.response = self.client.post(
      reverse('create'),
      self.bucketlist_data,
      format="json"
    )
  
  def test_api_create_bucketlist_item(self):
    """Test API POST"""
    self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

  def test_api_read_bucketlist_item(self):
    """Test API GET"""
    
    bucketlist = BucketList.objects.get()
    response = self.client.get(
            reverse('details'),
            kwargs={'pk': bucketlist.id}, format="json")
    
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertContains(response, bucketlist)


  def test_api_update_bucketlist_item(self):
    """Test API PUT"""
    bucketlist = Bucketlist.objects.get()
    change_bucketlist = {'name': 'Test new'}
    response = self.client.put(
            reverse('details'),
            change_bucketlist,
            kwargs={'pk': bucketlist.id},
            format="json")
    
    self.assertEqual(response.status_code, status.HTTP_200_OK)

  
  def test_api_delete_bucketlist_item(self):
    """Test API DELETE"""
    
    bucketlist = BucketList.objects.get()
    response = self.client.put(
            reverse('details'),
            change_bucketlist,
            kwargs={'pk': bucketlist.id},
            format="json")
    
    self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)