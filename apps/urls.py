from django.urls import path
from django.views.generic import TemplateView

from apps.views import RegisterView, UserLoginView, ChangePasswordView, EditProfileView, HomePage, ProductDetailView

urlpatterns = [
    path('', HomePage.as_view(), name='main'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('profile/edit/<int:pk>/', EditProfileView.as_view(), name='edit_profile'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/', ChangePasswordView.as_view(), name='password_change'),
]
