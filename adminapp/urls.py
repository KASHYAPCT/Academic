
from django.urls import path
from .import views

urlpatterns = [
    path('',views.Login,name="Loginuser"),
    path('home/',views.dashboard,name="dashboard"),
    path('logout/',views.logout_view, name='logout'),
    path('addstaff/',views.Addstaff,name="Addstaff"),
]
