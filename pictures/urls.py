from django.conf.urls import url
from . import views


urlpatterns=[
    url('^$',views.instagram,name = 'instagram'),
    url(r'^$',views.pictures_of_day,name='picturesToday'),
   

]

