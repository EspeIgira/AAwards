# # -*- coding: utf-8 -*-
# from __future__ import unicode_literals

from django.test import TestCase
from .models import Picture



class PictureTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.name = Picture(name = 'name')
        self.name.save()

        self.picture= Picture(name = 'picture', picture_Main_pic ='instagram/myprofile.jpg',bio='bio',user='user')
      
        
        # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.picture,Picture))

     
        self.name = Picture(name = 'name')
        self.name.save()


        self.name.add(self.name)


    def tearDown(self):
        Picture.objects.all().delete()
        


    def pictures_of_day(self):
        pictures = Picture.pictures()
        self.assertTrue(len(pictures)>0)

    def test_delete_method(self):
       self.name.save_picture()
       pictures = Picture.objects.all()
       self.assertTrue(len(pictures) > 0)

    def test_display_method(self):
        self.name.save_picture()
        pictures = Picture.objects.all()
        self.assertTrue(len(pictures) > 0)

    def test_update_method(self):
        self.name.save_picture()
        pictures = Picture.objects.all()
        self.assertTrue(len(pictures) > 0)
       









