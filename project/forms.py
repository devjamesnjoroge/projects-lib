from django import forms

from .models import Profile, Project

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'profile_pic', 'contact']
    exclude = ['user']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'image', 'link']
    exclude = ['user']