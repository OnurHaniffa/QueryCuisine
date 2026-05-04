from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.db import transaction
from django.db.models import Avg, Count
from django.shortcuts import render, redirect, get_object_or_404

from .forms import (
    RegisterForm, RestaurantForm, ReviewForm, ReviewReplyForm,
    MenuItemForm, ProfileForm,
)
from .models import (
    Restaurant, Review, ReviewReply, Favorite, MenuItem,
    Category, Location, UserProfile,
)


# ---------------- HOME ----------------
def home(request):
    # Top 3 by average rating, plus 3 newest. Simple and demoable.
    top_rated = Restaurant.objects.annotate(
        avg=Avg('reviews__rating')
    ).order_by('-avg')[:3]
    newest = Restaurant.objects.order_by('-created_at')[:3]
    return render(request, "home.html", {
        "top_rated": top_rated,
        "newest": newest,
    })


# ---------------- LIST + SEARCH + FILTER + SORT ----------------
def restaurant_list(request):
    restaurants = Restaurant.objects.all()

    q = request.GET.get("q", "")
    category = request.GET.get("category", "")
    location = request.GET.get("location", "")
    price = request.GET.get("price", "")
    sort = request.GET.get("sort", "")

    if q:
        restaurants = restaurants.filter(name__icontains=q)
    if category:
        restaurants = restaurants.filter(category_id=category)
    if location:
        restaurants = restaurants.filter(location_id=location)
    if price:
        restaurants = restaurants.filter(price_range=price)

    # Sorting. We use annotate(avg=Avg(...)) because average_rating is a
    # Python method on the model — order_by needs a real DB column.
    if sort == "rating":
        restaurants = restaurants.annotate(
            avg=Avg('reviews__rating')
        ).order_by('-avg')
    elif sort == "popular":
        restaurants = restaurants.annotate(
            review_count=Count('reviews')
        ).order_by('-review_count')
    elif sort == "newest":
        restaurants = restaurants.order_by('-created_at')
    elif sort == "cheap":
        restaurants = restaurants.order_by('price_range')

    return render(request, "restaurant_list.html", {
        "restaurants": restaurants,
        "categories": Category.objects.all(),
        "locations": Location.objects.all(),
    })


# ---------------- DETAIL ----------------
def restaurant_detail(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)
    reviews = restaurant.reviews.all()
    opening_hours = restaurant.opening_hours.all()
    menu_items = restaurant.menu_items.all()

    is_favorite = False
    user_review = None
    if request.user.is_authenticated:
        is_favorite = Favorite.objects.filter(
            user=request.user, restaurant=restaurant
        ).exists()
        user_review = reviews.filter(user=request.user).first()

    return render(request, "restaurant_detail.html", {
        "restaurant": restaurant,
        "reviews": reviews,
        "opening_hours": opening_hours,
        "menu_items": menu_items,
        "is_favorite": is_favorite,
        "user_review": user_review,
        "review_form": ReviewForm(),
        "reply_form": ReviewReplyForm(),
    })


# ---------------- RESTAURANT CRUD ----------------
@login_required
@transaction.atomic
def restaurant_create(request):
    if request.method == "POST":
        form = RestaurantForm(request.POST, request.FILES)
        if form.is_valid():
            restaurant = form.save(commit=False)
            restaurant.created_by = request.user
            restaurant.save()
            messages.success(request, f"'{restaurant.name}' was created.")
            return redirect("restaurant_detail", restaurant_id=restaurant.id)
    else:
        form = RestaurantForm()

    return render(request, "restaurant_form.html", {
        "form": form,
        "title": "Add Restaurant",
    })


@login_required
def restaurant_update(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)

    # Only the creator may edit.
    if restaurant.created_by != request.user:
        messages.error(request, "You can only edit your own restaurants.")
        return redirect("restaurant_detail", restaurant_id=restaurant.id)

    if request.method == "POST":
        form = RestaurantForm(request.POST, request.FILES, instance=restaurant)
        if form.is_valid():
            form.save()
            messages.success(request, f"'{restaurant.name}' was updated.")
            return redirect("restaurant_detail", restaurant_id=restaurant.id)
    else:
        form = RestaurantForm(instance=restaurant)

    return render(request, "restaurant_form.html", {
        "form": form,
        "title": f"Edit {restaurant.name}",
        "restaurant": restaurant,
    })


@login_required
def restaurant_delete(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)

    if restaurant.created_by != request.user:
        messages.error(request, "You can only delete your own restaurants.")
        return redirect("restaurant_detail", restaurant_id=restaurant.id)

    if request.method == "POST":
        name = restaurant.name
        restaurant.delete()
        messages.success(request, f"'{name}' was deleted.")
        return redirect("restaurant_list")

    return render(request, "restaurant_confirm_delete.html", {
        "restaurant": restaurant,
    })


# ---------------- REVIEWS ----------------
@login_required
def add_review(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)

    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            # update_or_create enforces "one review per user per restaurant"
            # without us writing a manual check.
            Review.objects.update_or_create(
                restaurant=restaurant,
                user=request.user,
                defaults={
                    "rating": form.cleaned_data["rating"],
                    "comment": form.cleaned_data["comment"],
                },
            )
            messages.success(request, "Your review was saved.")

    return redirect("restaurant_detail", restaurant_id=restaurant.id)


@login_required
def delete_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    restaurant_id = review.restaurant.id

    if review.user != request.user:
        messages.error(request, "You can only delete your own review.")
        return redirect("restaurant_detail", restaurant_id=restaurant_id)

    review.delete()
    messages.success(request, "Your review was deleted.")
    return redirect("restaurant_detail", restaurant_id=restaurant_id)


@login_required
def add_reply(request, review_id):
    review = get_object_or_404(Review, id=review_id)

    if request.method == "POST":
        form = ReviewReplyForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.review = review
            reply.user = request.user
            reply.save()
            messages.success(request, "Your reply was posted.")

    return redirect("restaurant_detail", restaurant_id=review.restaurant.id)


@login_required
def delete_reply(request, reply_id):
    reply = get_object_or_404(ReviewReply, id=reply_id)
    restaurant_id = reply.review.restaurant.id

    if reply.user != request.user:
        messages.error(request, "You can only delete your own reply.")
        return redirect("restaurant_detail", restaurant_id=restaurant_id)

    reply.delete()
    messages.success(request, "Your reply was deleted.")
    return redirect("restaurant_detail", restaurant_id=restaurant_id)


# ---------------- MENU ITEMS ----------------
@login_required
def menu_item_create(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)

    if restaurant.created_by != request.user:
        messages.error(request, "You can only add menu items to your own restaurants.")
        return redirect("restaurant_detail", restaurant_id=restaurant.id)

    if request.method == "POST":
        form = MenuItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.restaurant = restaurant
            item.save()
            messages.success(request, f"'{item.name}' was added to the menu.")
            return redirect("restaurant_detail", restaurant_id=restaurant.id)
    else:
        form = MenuItemForm()

    return render(request, "menu_item_form.html", {
        "form": form,
        "restaurant": restaurant,
        "title": f"Add Menu Item to {restaurant.name}",
    })


@login_required
def menu_item_update(request, menu_item_id):
    item = get_object_or_404(MenuItem, id=menu_item_id)

    if item.restaurant.created_by != request.user:
        messages.error(request, "You can only edit menu items on your own restaurants.")
        return redirect("restaurant_detail", restaurant_id=item.restaurant.id)

    if request.method == "POST":
        form = MenuItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, f"'{item.name}' was updated.")
            return redirect("restaurant_detail", restaurant_id=item.restaurant.id)
    else:
        form = MenuItemForm(instance=item)

    return render(request, "menu_item_form.html", {
        "form": form,
        "restaurant": item.restaurant,
        "title": f"Edit {item.name}",
    })


@login_required
def menu_item_delete(request, menu_item_id):
    item = get_object_or_404(MenuItem, id=menu_item_id)
    restaurant_id = item.restaurant.id

    if item.restaurant.created_by != request.user:
        messages.error(request, "You can only delete menu items on your own restaurants.")
        return redirect("restaurant_detail", restaurant_id=restaurant_id)

    if request.method == "POST":
        name = item.name
        item.delete()
        messages.success(request, f"'{name}' was removed from the menu.")
        return redirect("restaurant_detail", restaurant_id=restaurant_id)

    return render(request, "menu_item_confirm_delete.html", {
        "item": item,
    })


# ---------------- FAVORITES ----------------
@login_required
def toggle_favorite(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)

    favorite, created = Favorite.objects.get_or_create(
        user=request.user, restaurant=restaurant
    )
    if created:
        messages.success(request, f"'{restaurant.name}' added to favorites.")
    else:
        favorite.delete()
        messages.info(request, f"'{restaurant.name}' removed from favorites.")

    return redirect("restaurant_detail", restaurant_id=restaurant.id)


@login_required
def favorite_list(request):
    favorites = Favorite.objects.filter(user=request.user)
    return render(request, "favorites.html", {"favorites": favorites})


# ---------------- PROFILE ----------------
@login_required
def profile_view(request):
    profile, _ = UserProfile.objects.get_or_create(user=request.user)

    if request.method == "POST":
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated.")
            return redirect("profile")
    else:
        form = ProfileForm(instance=profile)

    my_reviews = Review.objects.filter(user=request.user)
    my_favorites = Favorite.objects.filter(user=request.user)
    my_restaurants = Restaurant.objects.filter(created_by=request.user)

    return render(request, "profile.html", {
        "profile": profile,
        "form": form,
        "my_reviews": my_reviews,
        "my_favorites": my_favorites,
        "my_restaurants": my_restaurants,
    })


# ---------------- AUTH ----------------
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


# ---------------- STATIC PAGES ----------------
def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")
