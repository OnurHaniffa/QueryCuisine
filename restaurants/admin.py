from django.contrib import admin
from .models import Category, Location, Restaurant, MenuItem, Review, ReviewReply, Favorite, UserProfile

admin.site.register(Category)
admin.site.register(Location)
admin.site.register(Restaurant)
admin.site.register(MenuItem)
admin.site.register(Review)
admin.site.register(ReviewReply)
admin.site.register(Favorite)
admin.site.register(UserProfile)
