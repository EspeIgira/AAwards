# # -*- coding: utf-8 -*-
# from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import ProjectForm,ProfileForm, SignUpForm
from .models import Project, Profile,Vote
from .email import send_welcome_email
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProjectSerializer
from rest_framework import status
from .permissions import IsAdminOrReadOnly
from django.views import generic



@login_required(login_url='/accounts/login/')
def aaward(request):
    
    project = Project.objects.all()
    profile = Profile.objects.all()
    print(profile)
    return render(request, 'Aaward.html',{'project':project,"profile":profile})



@login_required(login_url='/accounts/login/')
def projects_of_day(request):
    
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['your_title']
            description = form.cleaned_data['description']
            link = form.cleaned_data['link']
            # picture_Main_pic= form.cleaned_data['picture_Main_pic']
            recipient = SignUpRecipients(title = title,description = description,link=link)
            recipient.save()
            send_welcome_email(name,email)
            HttpResponseRedirect('projectsToday')
    else:
        form = SignUpForm()
  
    return render(request, 'all-projects/todays-projects.html', {"date": date,"project":project,"signupForm":form})


def profile(request,profile_id):
    profile = Profile.objects.get(id = profile_id)
    
    return render(request,'profile.html', {"profile":profile})

@login_required(login_url='/accounts/login/')
def newprofile(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
        return redirect('projectsToday')

    else:
        form = ProfileForm()
    return render(request, 'displayprofile.html', {"form": form})



@login_required(login_url='/accounts/login/')
def profile_view(request):

    current_user = request.user
    current_user.id
    profile = Profile.objects.get(user=current_user.id)
    
    print(profile.name)
    return render(request, 'profile_view.html',{"profile":profile})

#-----------------------------------------------------------------------------------------

def project(request,project_id):
    project = Project.objects.get(id = project_id)
    
    return render(request,"project.html", {"project":project})



@login_required(login_url='/accounts/login/')
def newproject(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = current_user
            project.save()
        return redirect('projectsToday')

    else:
        form = ProjectForm()
    return render(request, 'displayproject.html', {"form": form})

def projects_today(request):
    date = dt.date.today()
    projects = Project.todays_projects()
    form = ProjectForm()
    return render(request, 'all-projects/todays-projects.html', {"date": date, "projects": projects, "ProjectForm": form})


def projectspost(request):
    name = request.POST.get('your_name')
    email = request.POST.get('email')

    recipient = NewsLetterRecipients(name=name, email=email)
    recipient.save()
    send_welcome_email(name, email)
    data = {'success': 'You have been successfully added to mailing list'}
    return JsonResponse(data)


@login_required(login_url='/accounts/login/')
def detailsproject(request):

    current_user = request.user
    current_user.id
    project = Project.objects.all()
    return render(request, "detailsproject.html",{"project":project})


#search----------------------------------------------------------------------------------------------------------------------

def search_results(request):

    if 'title' in request.GET and request.GET["title"]:
        search_term = request.GET.get("title")
        titles = Project.search_title(search_term)
        message = f"{search_term}"

        return render(request, 'all-projects/search.html',{"message":message,"titles": titles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-projects/search.html',{"message":message})




#postman------------------------------------------------------------------------------------------------------------------------------

class MerchList(APIView):
    def get(self, request, format=None):
        all_merch = Project.objects.all()
        serializers =  ProjectSerializer(all_merch, many=True)
        return Response(serializers.data)
        permission_classes = (IsAdminOrReadOnly,)

    

    def post(self, request, format=None):
        serializers = ProjectSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class MerchDescription(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get_merch(self, pk):
        try:
            return MoringaMerch.objects.get(pk=pk)
        except MoringaMerch.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        merch = self.get_merch(pk)
        serializers = ProjectSerializer(merch)
        return Response(serializers.data)


    def put(self, request, pk, format=None):
        merch = self.get_merch(pk)
        serializers = ProjectSerializer(merch, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    
    def delete(self, request, pk, format=None):
        merch = self.get_merch(pk)
        merch.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
