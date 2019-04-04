# # -*- coding: utf-8 -*-
# from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import ProjectForm,ProfileForm, SignUpForm
from .models import Project, Profile
from .email import send_welcome_email
from django.http import JsonResponse


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




def search_results(request):

    if 'projectname' in request.GET and request.GET["projectname"]:
        search_term = request.GET.get("projectname")
        searched_projects = project.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'all-projects/search.html',{"message":message,"projects": searched_projects})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-projects/search.html',{"message":message})

