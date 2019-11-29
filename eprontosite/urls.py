from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^epronto/$', views.dashboard_home, name='dashboard_home'),
]