# # -*- coding: utf-8 -*-
# from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

class Profile(models.Model):
    name = models.CharField(max_length =60)
    picture_Main_pic = models.ImageField(upload_to='awwards/', blank=True) 
    bio = models.CharField(max_length =500)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.name


    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def update_profile(self):
        self.update()
    
    def display_profile(self):
        self.display()

    
    @classmethod
    def profile(cls):
        return Profile.objects.all()


    class Meta:
        ordering = ['name']




class Project(models.Model):
    title = models.CharField(max_length =30)
    picture_Main_pic = models.ImageField(upload_to='awwards/',null=True) 
    description = models.TextField()
    link = models.TextField()
    profile = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title


    def save_project(self):
        self.save()
    
   
    def display_project(self):
        self.display()

    def delete_project(self):
        self.delete()
    
    
    @classmethod
    def get_project(cls):
        return Project.objects.all()

    
    
# @classmethod
# def search_by_title(cls,search_term):
#     title = Project.objects.filter(title__icontains=search_term).all()
#     projects=None
#     for i in title:
#         print(i)
#         projects=cls.objects.filter(title=i.id)
#     return projects

    @classmethod
    def search_title(cls,search_term):
            titles = cls.objects.filter(title__icontains=search_term).all()
            return titles


class Meta:
    ordering = ['title']


class SignUpRecipients(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()


