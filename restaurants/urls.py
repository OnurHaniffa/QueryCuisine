from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('restaurants/', views.restaurant_list, name='restaurant_list'),
    path('restaurant/<int:restaurant_id>/', views.restaurant_detail, name='restaurant_detail'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),

    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]