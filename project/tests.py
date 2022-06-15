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

class ProjectTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.project = Project.objects.create(title='test title', description='test description', user=self.user)

    def test_project_creation(self):
        self.assertEqual(self.project.title, 'test title')
        self.assertEqual(self.project.description, 'test description')
        self.assertEqual(self.project.user.username, 'testuser')
    
    def test_project_str(self):
        self.assertEqual(self.project.__str__(), 'test title')
    