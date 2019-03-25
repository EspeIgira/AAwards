# # -*- coding: utf-8 -*-
# from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404,HttpResponseRedirect
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm, SignUpForm



# def instagram(request):
#     return HttpResponse('Instagram Clone _Welcome')

@login_required(login_url='/accounts/login/')
def instagram(request):
    return render(request, 'instagram.html')


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
  
    return render(request, 'all-pictures/instagram.html', {"date": date,"pictures":pictures,"signupForm":form})




def picture(request,picture_id):
    try:
        picture = Picture.objects.get(id = picture_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"all-pictures/instagram.html", {"picture":picture})


@login_required(login_url='/accounts/login/')
def newpicture(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            picture = form.save(commit=False)
            picture.user = current_user
            picture.save()
        return redirect('picturesToday')

    else:
        form = ProfileForm()
    return render(request, 'profile.html', {"form": form})

