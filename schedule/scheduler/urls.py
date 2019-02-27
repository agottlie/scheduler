from django.urls import path

from scheduler import views

urlpatterns = [
    path('', views.home, name='home'),
    path('appointment/new', views.new_appointment, name='new_appointment'),
    path('client/new', views.new_client, name='new_client'),
    path('client/directory', views.directory, name='directory'),
    path('statistics', views.statistics, name='statistics'),
]