# # -*- coding: utf-8 -*-
# from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required.


# def instagram(request):
#     return HttpResponse('Instagram Clone _Welcome')

def instagram(request):
    return render(request, 'instagram.html')


def pictures_of_day(request):
    date = dt.date.today()
    pictures = Picture.objects.all()

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            print('valid')
    else:
        form = SignUpForm()
  
    return render(request, 'all-pictures/todays_pictures.html', {"date": date,"pictures":pictures,"signupForm":form})


def picture(request,picture_id):
    try:
        picture = Picture.objects.get(id = picture_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"all-pictures/pictures.html", {"picture":picture})