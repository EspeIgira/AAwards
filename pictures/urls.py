from django.conf.urls import url
from . import views
from mysite.core import views as core_views

urlpatterns=[
    url('^$',views.instagram,name = 'instagram'),
    url(r'^$',views.pictures_of_day,name='picturesToday'),
    url(r'^signup/$', core_views.signup, name='signup'),

]

