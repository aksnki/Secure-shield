"""M_D_threat_dectection URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from myapp import views

urlpatterns = [
    path('login/', views.login),
    path('login_post/', views.login_post),
    path('logout/', views.logout),
    path('forgotpassword/', views.forgotpassword),
    path('forgotpassword_post/', views.forgotpassword_post),
    path('admin_home/', views.admin_home),
    path('admin_change_password/',views.admin_change_password),
    path('admin_change_password_post/',views.admin_change_password_post),
    path('admin_send_replay/<id>',views.admin_send_replay),
    path('admin_send_replay_post/',views.admin_send_replay_post),
    path('admin_view_complaint/', views.admin_view_complaint),
    path('admin_view_complaint_post/', views.admin_view_complaint_post),
    path('admin_view_app_review/',views.admin_view_app_review),
    path('admin_view_app_review_post/',views.admin_view_app_review_post),
    path('admin_view_customer/', views.admin_view_customer),
    path('admin_view_customer_post/', views.admin_view_customer_post),
    path('user_change_password/', views.user_change_password),
    path('user_home/', views.user_home),
    path('user_change_password_post/', views.user_change_password_post),
    path('user_edit_profile/',views.user_edit_profile),
    path('user_edit_profile_post/',views.user_edit_profile_post),
    path('user_image_forgery/', views.user_image_forgery),
    path('user_image_forgery_post/', views.user_image_forgery_post),
    path('user_mail_spamming/', views.user_mail_spamming),
    path('user_mail_spamming_post/', views.user_mail_spamming_post),
    path('user_send_complaint/', views.user_send_complaint),
    path('user_send_complaint_post/', views.user_send_complaint_post),
    path('user_send_review/', views.user_send_review),
    path('user_send_review_post/', views.user_send_review_post),
    path('user_url/', views.user_url),
    path('user_url_post/', views.user_url_post),
    path('user_reg/', views.user_reg),
    path('user_reg_post/', views.user_reg_post),
    path('user_view_profile/',views.user_view_profile),
    path('user_edit_profile/', views.user_edit_profile),
    path('user_edit_profile_post/', views.user_edit_profile_post),
    path('user_view_replay/', views.user_view_replay),
    path('user_view_replay_post/', views.user_view_replay_post),

]
