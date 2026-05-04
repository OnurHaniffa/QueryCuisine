from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Review, ReviewReply, Restaurant, MenuItem, UserProfile


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = [
            'name', 'description', 'address', 'phone',
            'category', 'location', 'price_range', 'photo',
        ]


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']


class ReviewReplyForm(forms.ModelForm):
    class Meta:
        model = ReviewReply
        fields = ['text']


class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ['name', 'description', 'price', 'category']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio']
