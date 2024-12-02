
from django.urls import path
from .import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('',views.Login,name="Loginuser"),
    path('home/',views.dashboard,name="dashboard"),
    path('logout/',views.logout_view, name='logout'),
    path('addstaff/',views.Addstaff,name="Addstaff"),
     path('accounts/password_change/', auth_views.PasswordChangeView.as_view(template_name='admin_app/pages/password_change.html'), name='password_change'),
    path('accounts/password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='admin_app/pages/password_change_done.html'), name='password_change_done')
]
