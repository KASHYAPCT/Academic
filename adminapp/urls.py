
from django.urls import path
from .import views

urlpatterns = [
    path('',views.Login,name="Loginuser"),
    path('home/',views.home,name="home")
]
