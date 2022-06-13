from django.shortcuts import redirect, render
from django.contrib.auth.models import User

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

    
