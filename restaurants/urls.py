from django.urls import path
from . import views

urlpatterns = [
    # HOME
    path('', views.home, name='home'),

    # READ
    path('restaurants/', views.restaurant_list, name='restaurant_list'),
    path('restaurant/<int:restaurant_id>/', views.restaurant_detail, name='restaurant_detail'),

    # CREATE
    path('restaurant/create/', views.restaurant_create, name='restaurant_create'),

    # UPDATE
    path('restaurant/<int:restaurant_id>/edit/', views.restaurant_update, name='restaurant_update'),

    # DELETE
    path('restaurant/<int:restaurant_id>/delete/', views.restaurant_delete, name='restaurant_delete'),

    # FAVORITE
    path('favorite/<int:restaurant_id>/', views.toggle_favorite, name='toggle_favorite'),

    # AUTH
    path('register/', views.register_view, name='register'),

    # STATIC
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]