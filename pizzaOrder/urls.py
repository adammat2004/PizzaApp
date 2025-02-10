from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.home, name="home"),
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('create_pizza/', views.create_pizza, name='create_pizza'),
    path('delivery_details/<uuid:pizza_order_id>/', views.delivery_details, name='delivery_details'),
    path('order_complete/<uuid:pizza_order_id>/', views.order_complete, name='order_complete'),
    ]