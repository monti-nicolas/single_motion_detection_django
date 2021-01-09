from django.urls import path
from . import views

app_name = 'motion_detect'
urlpatterns = [
    #path('', views.capture, name='capture'),
    path('motion/', views.index, name='index'),
    path('video_feed/', views.video_feed, name='video_feed'),
]
