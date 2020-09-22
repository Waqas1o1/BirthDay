from django.urls import path
from . import  views
urlpatterns = [
    path('',views.index),
    path('home/',views.home),
    path('home/<int:pk>',views.Detail),    
]
