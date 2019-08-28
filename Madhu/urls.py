"""Madhu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views
from django.views.generic import TemplateView,ListView,DetailView
from app.models import Patient
from app.models import Detalis
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path("show/", views.show),
    path("viewall/", views.Viewall.as_view(), name="Viewall"),
    path('viewallids/', views.AllPatientIds.as_view(), name='allids'),
    path('onedetails<int:pk>/',views.OnePatient.as_view(), name='oneemp'),
    #path('onedetails<int:pk>/',DetailView.as_view(template_name="OnePatient.html",model=Patient), name='oneemp'),
    path('home/', views.home, name='home'),
    path(r"search/", views.search, name="search"),
    path('index1/',TemplateView.as_view(template_name="show.html"),name="show"),
    path('index2/',views.index2),
    path('index3/',TemplateView.as_view(template_name="show1.html"),name="show1"),
    path('index4/',views.Index4.as_view(),name="all"),
    path("index5/",views.index5),
    path('image_upload/', views.pre, name='image_upload'),
   # path('success/', views.success, name='success'),

]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
        urlpatterns += staticfiles_urlpatterns()



