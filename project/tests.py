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

class RateTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.project = Project.objects.create(title='test title', description='test description', user=self.user)
        self.rate = Rate.objects.create(user=self.user, project=self.project, design_rate=5, usability_rate=5, content_rate=5)

    def test_rate_creation(self):
        self.assertEqual(self.rate.user.username, 'testuser')
        self.assertEqual(self.rate.project.title, 'test title')
        self.assertEqual(self.rate.design_rate, 5)
        self.assertEqual(self.rate.usability_rate, 5)
        self.assertEqual(self.rate.content_rate, 5)
        self.assertEqual(self.rate.total_rate, 15)

    def test_rate_str(self):
        self.assertEqual(self.rate.__str__(), 'testuser')