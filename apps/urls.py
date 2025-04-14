from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from apps.views import LoginView, ProfileSettingsView, register_view, category_view,  product_detail_view

urlpatterns = [
    path('', register_view, name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profilesettings/', ProfileSettingsView, name='profile_settings'),
    path('category/', category_view, name='category'),
    path('product/', product_detail_view, name='product'),
]
