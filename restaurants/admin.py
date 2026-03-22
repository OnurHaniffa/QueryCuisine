from django.contrib import admin                             
from .models import Category, Location, OpeningHours,Restaurant, MenuItem, Review, ReviewReply, Favorite, UserProfile

                                                               
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):                       
      list_display = ['name', 'slug']                        
      search_fields = ['name']


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
      list_display = ['city', 'district']
      search_fields = ['city', 'district']                     
      list_filter = ['city']                                   
                                                               
                                                               
@admin.register(Restaurant)                                  
class RestaurantAdmin(admin.ModelAdmin):                     
      list_display = ['name', 'category', 'location',          
  'price_range', 'created_by', 'created_at']                   
      search_fields = ['name', 'description']                  
      list_filter = ['category', 'price_range', 'location']    
                                                             
                                                               
@admin.register(OpeningHours)                              
class OpeningHoursAdmin(admin.ModelAdmin):
      list_display = ['restaurant', 'day_of_week', 'open_time',
   'close_time']
      list_filter = ['day_of_week', 'restaurant']              
                                                               
  
@admin.register(MenuItem)                                    
class MenuItemAdmin(admin.ModelAdmin):                     
      list_display = ['name', 'restaurant', 'price',
  'category']
      search_fields = ['name']
      list_filter = ['category', 'restaurant']                 
  
                                                               
@admin.register(Review)                                    
class ReviewAdmin(admin.ModelAdmin):
      list_display = ['restaurant', 'user', 'rating',
  'created_at']
      search_fields = ['comment']
      list_filter = ['rating', 'created_at']                   
  
                                                               
@admin.register(ReviewReply)                               
class ReviewReplyAdmin(admin.ModelAdmin):
      list_display = ['review', 'user', 'created_at']
                                                               
                                                               
@admin.register(Favorite)                                    
class FavoriteAdmin(admin.ModelAdmin):                       
      list_display = ['user', 'restaurant', 'added_at']      
      list_filter = ['user']                                   
                                                               
                                                               
@admin.register(UserProfile)                                 
class UserProfileAdmin(admin.ModelAdmin):                  
      list_display = ['user', 'bio']                           
      search_fields = ['user__username']