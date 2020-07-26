from django.urls import path
from . import views

urlpatterns = [
    path('',views.hi, name="home"),
    path('count/',views.count,name="counts"),
    path('about/',views.about,name="about"),
]
