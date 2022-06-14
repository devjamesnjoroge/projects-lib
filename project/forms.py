from django import forms

from .models import Profile, Project, Rate

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

class RateForm(forms.ModelForm):
    class Meta:
        model = Rate
        fields = ['design_rate', 'usability_rate', 'content_rate']
    exclude = ['user', 'project']