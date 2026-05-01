from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .models import Restaurant, Review, UserProfile
from .forms import ReviewForm, RegisterForm, RestaurantForm

def home(request):
    restaurants = Restaurant.objects.all()
    return render(request, "home.html", {"restaurants": restaurants})


def restaurant_detail(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)
    reviews = restaurant.reviews.all()
    opening_hours = restaurant.opening_hours.all()
    menu_items = restaurant.menu_items.all()
    form = ReviewForm()
    already_reviewed = False

    if request.user.is_authenticated:
        already_reviewed = Review.objects.filter(restaurant=restaurant, user=request.user).exists()

        if request.method == "POST" and not already_reviewed:
            form = ReviewForm(request.POST)
            if form.is_valid():
                review = form.save(commit=False)
                review.restaurant = restaurant
                review.user = request.user
                review.save()
                return redirect('restaurant_detail', restaurant_id=restaurant.id)

    return render(request, "detail.html", {
        "restaurant": restaurant,
        "reviews": reviews,
        "opening_hours": opening_hours,
        "menu_items": menu_items,
        "form": form,
        "already_reviewed": already_reviewed,
    })


def restaurant_list(request):
    restaurants = Restaurant.objects.all()
    return render(request, "restaurant_list.html", {"restaurants": restaurants})


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")


def register_view(request):
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user)
            login(request, user)
            messages.success(request, f"Welcome, {user.username}! Your account is ready.")
            return redirect("home")
    else:
        form = RegisterForm()
    return render(request, "register.html", {"form": form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect("home")
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form})


def logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect("home")
@login_required
def restaurant_create(request):
    if request.method == 'POST':
        form = RestaurantForm(request.POST, request.FILES)
        if form.is_valid():
            restaurant = form.save(commit=False)
            restaurant.created_by = request.user
            restaurant.save()
            return redirect('restaurant_list')
    else:
        form = RestaurantForm()

    return render(request, 'restaurant_form.html', {'form': form})
@login_required
def restaurant_edit(request, pk):
    restaurant = get_object_or_404(Restaurant, pk=pk)

    if restaurant.created_by != request.user:
        return redirect('restaurant_list')

    if request.method == 'POST':
        form = RestaurantForm(request.POST, request.FILES, instance=restaurant)
        if form.is_valid():
            form.save()
            return redirect('restaurant_detail', restaurant_id=restaurant.id)
    else:
        form = RestaurantForm(instance=restaurant)

    return render(request, 'restaurant_form.html', {'form': form})
@login_required
def restaurant_delete(request, pk):
    restaurant = get_object_or_404(Restaurant, pk=pk)

    if restaurant.created_by != request.user:
        return redirect('restaurant_list')

    restaurant.delete()
    return redirect('restaurant_list')
