from django.urls import path
from core import views

urlpatterns = [
    path('', views.home, name='home'),
    path('announcements_list/', views.announcements_list, name='announcements_list'),
    path('announcements_detail/<int:id>/', views.announcements_detail, name='announcements_detail'),
]
