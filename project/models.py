from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    bio = models.TextField(blank=True)
    profile_pic = CloudinaryField('image')
    contact = models.CharField(max_length=255)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
