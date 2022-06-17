from django.shortcuts import redirect, render
from django.contrib.auth.models import User

from project.permissions import IsAdminOrReadOnly
from .models import Profile, Project, Rate
from . forms import ProfileForm, ProjectForm, RateForm
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ProfileSerializer, ProjectSerializer
from rest_framework import status

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
        return redirect('/accounts/login/')
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

def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = request.user
            project.save()
            return redirect('index')
    else:
        form = ProjectForm()
    return render(request, 'add_project.html', {'form': form})

def projects(request):
    projects = Project.objects.all()
    print(projects)
    return render(request, 'project.html', {'projects': projects})

def project_details(request, pid):
    project = Project.objects.get(id=pid)
    ratings = Rate.objects.filter(project__id=pid)
    return render(request, 'project_details.html', {'project': project, 'ratings': ratings})

def rate(request, pid):
    if Rate.objects.filter(user=request.user, project__id = pid).exists():
        rated = True
    else:
        rated = False
    if request.method == 'POST':
        form = RateForm(request.POST)
        if form.is_valid():
            rate = form.save(commit=False)
            rate.user = request.user
            rate.project = Project.objects.get(id=pid)
            rate.save()
            return redirect('index')
    else:
        form = RateForm()
    return render(request, 'rate.html', {'form': form, 'rated': rated})


class ProfileList(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get(self, request):
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProjectList(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get(self, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)


    def post(self, request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)