from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    url('^$',views.instagram,name = 'instagram'),
    url(r'^$',views.pictures_of_day,name='picturesToday'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^new/picture$', views.newpicture, name='newpicture'),
    url(r'^profile/',views.picture,name ='profile'),
    url(r'^view/profile/(\d+)', views.profile_view, name='profile_view'),
    url(r'^picture/',views.picture,name ='picture'),
    url(r'^picture/',views.addpicture,name ='addpicture'),


    # url(r'^new/profile$', views.newprofile, name='newprofile'),
    # url(r'^picture/(\d+)',views.picture,name ='picture'),
    

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

