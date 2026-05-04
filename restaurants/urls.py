from django.urls import path
from . import views

urlpatterns = [
    # HOME + LIST + DETAIL
    path('', views.home, name='home'),
    path('restaurants/', views.restaurant_list, name='restaurant_list'),
    path('restaurant/<int:restaurant_id>/', views.restaurant_detail, name='restaurant_detail'),

    # RESTAURANT CRUD
    path('restaurant/create/', views.restaurant_create, name='restaurant_create'),
    path('restaurant/<int:restaurant_id>/edit/', views.restaurant_update, name='restaurant_update'),
    path('restaurant/<int:restaurant_id>/delete/', views.restaurant_delete, name='restaurant_delete'),

    # REVIEWS + REPLIES
    path('restaurant/<int:restaurant_id>/review/add/', views.add_review, name='add_review'),
    path('review/<int:review_id>/delete/', views.delete_review, name='delete_review'),
    path('review/<int:review_id>/reply/', views.add_reply, name='add_reply'),
    path('reply/<int:reply_id>/delete/', views.delete_reply, name='delete_reply'),

    # MENU ITEMS
    path('restaurant/<int:restaurant_id>/menu/add/', views.menu_item_create, name='menu_item_create'),
    path('menu/<int:menu_item_id>/edit/', views.menu_item_update, name='menu_item_update'),
    path('menu/<int:menu_item_id>/delete/', views.menu_item_delete, name='menu_item_delete'),

    # FAVORITES
    path('favorite/<int:restaurant_id>/', views.toggle_favorite, name='toggle_favorite'),
    path('favorites/', views.favorite_list, name='favorite_list'),

    # PROFILE
    path('profile/', views.profile_view, name='profile'),

    # AUTH
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # STATIC PAGES
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]
