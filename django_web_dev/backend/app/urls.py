from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views

from app import views
urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('accounts/login/', views.login, name='login_redirect'),
    path('logout/', views.logout_view, name='logout'),
    path('addpost/', views.addpost_view, name='addpost'),
    path('editpost/<int:post_id>/', views.editpost_view, name='editpost'),
    path('deletepost/<int:post_id>/', views.deletepost_view, name='deletepost'),
    path('admin-view/',views.admin_view,name='admin_view'),
    path('password-reset/', 
         auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html'), 
         name='password_reset'),
         
    path('password-reset/done/', 
         auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), 
         name='password_reset_done'),
         
    path('reset/<uidb64>/<token>/', 
         auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), 
         name='password_reset_confirm'),
         
    path('reset/done/', 
         auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), 
         name='password_reset_complete'),
]