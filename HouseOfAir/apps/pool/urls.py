from django.urls import path
from . import views

urlpatterns = [
    path('', views.inter, name = "inter"),
    path('report/', views.rep, name = "rep"),
]
