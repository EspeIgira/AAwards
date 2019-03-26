# # -*- coding: utf-8 -*-
# from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import PictureForm,ProfileForm, SignUpForm
from .models import Picture, Profile


# def instagram(request):
#     return HttpResponse('Instagram Clone _Welcome')

@login_required(login_url='/accounts/login/')
def instagram(request):
    
    pictures = Picture.objects.all()
    profile = Profile.objects.all()
    print(profile)
    return render(request, 'instagram.html',{'pictures':pictures,"profile":profile})

@login_required(login_url='/accounts/login/')
def pictures_of_day(request):
    
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            profilepic = form.cleaned_data['profilepic']
            bio=HTMLField()
            recipient = SignUpRecipients(name = name,profilepic =profilepic,bio=bio)
            recipient.save()
            HttpResponseRedirect('pictures_today')
    else:
        form = SignUpForm()
  
    return render(request, 'all-pictures/todays_pictures.html', {"date": date,"pictures":pictures,"signupForm":form})


def picture(request,picture_id):
    picture = Picture.objects.get(id = picture_id)
    
    return render(request,"all-pictures/pictures.html", {"picture":picture})



@login_required(login_url='/accounts/login/')
def newpicture(request):
    current_user = request.user
    if request.method == 'POST':
        form = PictureForm(request.POST, request.FILES)
        if form.is_valid():
            picture = form.save(commit=False)
            picture.user = current_user
            picture.save()
        return redirect('picturesToday')

    else:
        form = PictureForm()
    return render(request, 'picture.html', {"form": form})


@login_required(login_url='/accounts/login/')
def newprofile(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
        return redirect('picturesToday')

    else:
        form = ProfileForm()
    return render(request, 'profile.html', {"form": form})



@login_required(login_url='/accounts/login/')
def profile_view(request):

    current_user = request.user
    current_user.id
    profile = Profile.objects.get(user=current_user.id)
    
    print(profile.name)
    return render(request, 'profile_view.html',{"profile":profile})


@login_required(login_url='/accounts/login/')
def addpicture(request):

    current_user = request.user
    current_user.id
    pictures = Picture.objects.all()
    return render(request, 'addpicture.html',{"pictures":pictures})



def search_results(request):

    if 'name' in request.GET and request.GET["name"]:
        search_term = request.GET.get("name")
        searched_pictures = Picture.search_by_name(search_term)
        message = f"{search_term}"

        return render(request, 'all-pictures/search.html',{"message":message,"pictures": searched_pictures})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-pictures/search.html',{"message":message})

