from django.urls import path, include
from . import views

urlpatterns = [
     path('', views.home, name='home'),
     path('about/', views.about, name = 'about'),
     # route for doves index
     path('doves/', views.doves_index, name='index'),
     path('doves/create/', views.DoveCreate.as_view(), name='dove_create'),
     path('doves/<int:dove_id>/', views.doves_detail, name ='detail'),
     path('doves/<int:pk>/update/', views.DoveUpdate.as_view(), name='dove_update'),
     path('doves/<int:pk>/delete/', views.DoveDelete.as_view(), name='dove_delete'),
     path('doves/<int:dove_id>/add_feeding/', views.add_feeding, name='add_feeding'),
     # associate a toy with a dove (M:M)
     path('doves/<int:dove_id>/assoc_toy/<int:toy_id>/', views.assoc_toy, name='assoc_toy'),
     # unassociate a toy and dove
     path('dove/<int:dove_id>/unassoc_toy/<int:toy_id>/', views.unassoc_toy, name='unassoc_toy'),
     ## photo unit missing
     path('toys/', views.ToyList.as_view(), name='toys_index'),
     path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toys_detail'),
     path('toys/create/', views.ToyCreate.as_view(), name='toys_create'),
     path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toys_update'),
     path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toys_delete'),
     path('accounts/', include('django.contrib.auth.urls')),
     path('accounts/signup', views.signup, name='signup'),

]