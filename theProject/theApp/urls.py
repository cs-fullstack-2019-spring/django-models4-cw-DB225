from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('mom/', views.getmom, name="mom"),
    path('child/', views.getchild, name="mom"),
]