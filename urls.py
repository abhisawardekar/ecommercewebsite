from os import name
from django.contrib import auth
from django.urls import path
from django.views.generic.base import View
from . import views
from django.contrib.auth import authenticate, views as auth_views
from .forms import LoginForm, PasswordChangeForm, UserPasswordResetForm, UserSetPasswordForm


urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('product_detail/<int:pk>/',
         views.ProductDetailView.as_view(), name='product_detail'),
    path('profile/', views.UserProfile.as_view(),
         name='user_profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    path('accounts/login', auth_views.LoginView.as_view(template_name='app/login.html',
                                                                      authentication_form=LoginForm), name='login'),
    path('accounts/logout/',
         auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('registration/', views.RegistrationView.as_view(), name='registration'),
    path('checkout/', views.checkout, name='checkout'),
    path('orderplaced/', views.order_placed, name='orderplaced'),
]
