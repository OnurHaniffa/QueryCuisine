from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('restaurants/', views.restaurant_list, name='restaurant_list'),
    path('restaurant/<int:restaurant_id>/', views.restaurant_detail, name='restaurant_detail'),

    # CRUD
    path('restaurant/create/', views.restaurant_create, name='restaurant_create'),
    path('restaurant/update/<int:restaurant_id>/', views.restaurant_update, name='restaurant_update'),
    path('restaurant/delete/<int:restaurant_id>/', views.restaurant_delete, name='restaurant_delete'),

    # FAVORITE
    path('favorite/<int:restaurant_id>/', views.toggle_favorite, name='toggle_favorite'),
    path('favorites/', views.favorite_list, name='favorite_list'),

    # AUTH
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),

    # STATIC
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),

    path('review/add/<int:restaurant_id>/', views.add_review, name='add_review'),
]