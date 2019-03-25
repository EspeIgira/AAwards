from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    url('^$',views.instagram,name = 'instagram'),
    url(r'^$',views.pictures_of_day,name='picturesToday'),
    url(r'^picture/(\d+)',views.picture,name ='picture'),
    url(r'^new/picture$', views.newpicture, name='newpicture')
   

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

