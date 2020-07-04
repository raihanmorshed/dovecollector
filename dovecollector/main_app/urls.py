from django.urls import path
from . import views

urlpatterns = [
     path('', views.home, name='home'),
     path('about/', views.about, name = 'about'),
     # route for doves index
     path('doves/', views.doves_index, name='index'),

]