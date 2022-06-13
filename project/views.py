from django.shortcuts import redirect, render
from django.contrib.auth.models import User

from .models import Profile

from . forms import ProfileForm

# Create your views here.

def index(request):
    return render(request, 'index.html')

def create_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        user = User.objects.create_user(username, email, password)
        user.save()
        return render(request, 'index.html')
    return render(request, 'registration/signup.html')


def create_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('index')
    else:
        form = ProfileForm()
    return render(request, 'profile.html', {'form': form})

def profile_display(request, uname):
    if Profile.objects.filter(user__username = uname).exists():
        profile = Profile.objects.get(user__username = uname)
    else:
        profile = None
    return render(request, 'profile_display.html', {'profile': profile})

def profile_edit(request, uname):
    if uname != request.user.username:
        return render(request, '403.html')
    if Profile.objects.filter(user__username = uname).exists():
        profile = Profile.objects.get(user__username = uname)
    else:
        profile = None
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile_display', uname=uname)
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'profile.html', {'form': form})