# # -*- coding: utf-8 -*-
# from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField


class Profile(models.Model):
    name = models.CharField(max_length =60)
    picture_Main_pic = models.ImageField(upload_to='instagram/', blank=True) 
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


    class Meta:
        ordering = ['name']

class Picture(models.Model):
    
    name = models.CharField(max_length =30)
    picture_Main_pic = models.ImageField(upload_to='instagram/',null=True) 
    likes = models.IntegerField(default=0)
    comments = models.CharField(max_length =100)
    caption = models.CharField(max_length =300)
    profile = models.ForeignKey(User,on_delete=models.CASCADE)
    


    def __str__(self):
        return self.name

    def save_picture(self):
        self.save()
    
   
    def display_picture(self):
        self.display()

    def delete_picture(self):
        self.delete()
    
    
    @classmethod
    def get_picture(cls,id):
        return Picture.objects.get(id=id)



    @classmethod
    def search_by_name(cls,search_term):
        name = Picture.objects.filter(name__icontains=search_term).all()
        pictures=None
        for i in name:
            print(i)
            pictures=cls.objects.filter(name=i.id)
        return pictures
 

    class Meta:
        ordering = ['name']

    
    
class Follow(models.Model):
    
    follower = models.IntegerField(default =30)
    following = models.IntegerField(default =30)
    profile = models.ForeignKey(Profile, null=True, blank=True)

    def __str__(self):
        return self.follower 

    def save_follower(self):
        self.save()

    def delete_follower(self):
        self.delete()

class Likes(models.Model):
    
    name = models.CharField(max_length =60)
    
    def __str__(self):
        return self.name 

    def save_likes(self):
        self.save()

    def delete_likes(self):
        self.delete()

class Comment(models.Model):
    
    comments = models.CharField(max_length =30)
    picture = models.ForeignKey(Picture, null=True, blank=True)
    # user = models.ForeignKey(Picture, null=True, blank=True)
    
    def __str__(self):
        return self.comments

    def save_comment(self):
        self.save()

    def delete_comment(self):
        self.delete()


    @classmethod
    def search_by_name(cls,search_term):
        pictures = cls.objects.filter(name__icontains=search_term)
        return pictures

class SignUpRecipients(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()
