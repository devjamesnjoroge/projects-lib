from django.test import TestCase
from .models import *

# Create your tests here.

class ProfileTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.profile = Profile.objects.create(user=self.user, bio='test bio', contact='test contact')

    def test_profile_creation(self):
        self.assertEqual(self.profile.bio, 'test bio')
        self.assertEqual(self.profile.contact, 'test contact')
        self.assertEqual(self.profile.user.username, 'testuser')

    def test_profile_str(self):
        self.assertEqual(self.profile.__str__(), 'testuser')

    