from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
    path('', views.contect_list, name='contect_list'),  
    path('add/', views.add_contect, name='add_contect'),
    path('update/<int:pk>/', views.update_contect, name='update_contect'), 
    path('delete/<int:pk>/', views.delete_contect, name='delete_contect'),
]
