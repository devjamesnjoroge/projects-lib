from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Profile(models.Model):
    bio = models.TextField(blank=True)
    profile_pic = CloudinaryField('image')
    contact = models.CharField(max_length=255)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = CloudinaryField('image')
    link = models.URLField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Rate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    design_rate = models.PositiveIntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(10)])
    usability_rate = models.PositiveIntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(10)])
    content_rate = models.PositiveIntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(10)])
    total_rate = models.PositiveIntegerField(default=0)
    def save(self, *args, **kwargs):
        self.total_rate = self.design_rate + self.usability_rate + self.content_rate
        super(Rate, self).save(*args, **kwargs)

    def __str__(self):
        return self.user.username