from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    url('^$',views.aaward,name = 'aaward'),
    url(r'^$',views.projects_of_day,name='projectsToday'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^profile/(\d+)',views.project,name ='profile'),#profile---
    url(r'^new/profile$', views.newprofile, name='newprofile'),#new profile---
    url(r'^view/profile$', views.profile_view, name='profile_view'),#view profile--
    url(r'^project/(\d+)',views.project,name ='project'),#project ##
    url(r'^new/project$', views.newproject, name='newproject'),#new project ##
    url(r'^view/project$',views.detailsproject,name ='detailsproject'),#details project ##
    url(r'^ajax/projects_today/$', views.projects_today, name='projects_today'),#ajax//
    url(r'^api/merch/$', views.MerchList.as_view()),
    url(r'api/merch/merch-id/(?P<pk>[0-9]+)/$',views.MerchDescription.as_view()),

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

