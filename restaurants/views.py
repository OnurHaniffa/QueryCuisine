from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect, get_object_or_404

from .models import Restaurant, Favorite, Review
from .models import Category, Location


# =========================
# HOME
# =========================
def home(request):
    restaurants = Restaurant.objects.all()[:6]
    return render(request, "home.html", {"restaurants": restaurants})


# =========================
# LIST + SEARCH + FILTER + SORT
# =========================
def restaurant_list(request):
    restaurants = Restaurant.objects.all()

    q = request.GET.get("q")
    category = request.GET.get("category")
    location = request.GET.get("location")
    price = request.GET.get("price")
    sort = request.GET.get("sort")

    if q:
        restaurants = restaurants.filter(name__icontains=q)

    if category:
        restaurants = restaurants.filter(category_id=category)

    if location:
        restaurants = restaurants.filter(location_id=location)

    if price:
        restaurants = restaurants.filter(price_range=price)

    if sort == "new":
        restaurants = restaurants.order_by("-id")
    elif sort == "rating":
        restaurants = restaurants.order_by("-average_rating")
    elif sort == "cheap":
        restaurants = restaurants.order_by("price_range")

    return render(request, "restaurant_list.html", {
        "restaurants": restaurants,
        "categories": Category.objects.all(),
        "locations": Location.objects.all()
    })
# =========================
# DETAIL
# =========================
def restaurant_detail(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)

    is_favorite = False
    if request.user.is_authenticated:
        is_favorite = Favorite.objects.filter(
            user=request.user,
            restaurant=restaurant
        ).exists()

    reviews = Review.objects.filter(restaurant=restaurant)

    return render(request, "restaurant_detail.html", {
        "restaurant": restaurant,
        "is_favorite": is_favorite,
        "reviews": reviews
    })


# =========================
# CREATE
# =========================
@login_required
def restaurant_create(request):
    if request.method == "POST":
        Restaurant.objects.create(
            name=request.POST.get("name"),
            description=request.POST.get("description"),
        )
        messages.success(request, "Restaurant created!")
        return redirect("restaurant_list")

    return render(request, "restaurant_form.html")


# =========================
# UPDATE
# =========================
@login_required
def restaurant_update(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)

    if request.method == "POST":
        restaurant.name = request.POST.get("name")
        restaurant.description = request.POST.get("description")
        restaurant.save()

        messages.success(request, "Restaurant updated!")
        return redirect("restaurant_detail", restaurant_id=restaurant.id)

    return render(request, "restaurant_form.html", {"restaurant": restaurant})


# =========================
# DELETE
# =========================
@login_required
def restaurant_delete(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)

    if request.method == "POST":
        restaurant.delete()
        messages.success(request, "Restaurant deleted!")
        return redirect("restaurant_list")  # 🔥 BURAYI DÜZELTTİM

    return render(request, "restaurant_confirm_delete.html", {"restaurant": restaurant})


# =========================
# FAVORITE TOGGLE
# =========================
@login_required
def toggle_favorite(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)

    favorite, created = Favorite.objects.get_or_create(
        user=request.user,
        restaurant=restaurant
    )

    if not created:
        favorite.delete()
        messages.info(request, "Removed from favorites")
    else:
        messages.success(request, "Added to favorites")

    return redirect("restaurant_detail", restaurant.id)


# =========================
# FAVORITE LIST
# =========================
@login_required
def favorite_list(request):
    favorites = Favorite.objects.filter(user=request.user)
    return render(request, "favorites.html", {"favorites": favorites})


# =========================
# ADD REVIEW
# =========================
@login_required
def add_review(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)

    if request.method == "POST":
        rating = request.POST.get("rating")
        comment = request.POST.get("comment")

        Review.objects.update_or_create(
            restaurant=restaurant,
            user=request.user,
            defaults={
                "rating": rating,
                "comment": comment
            }
        )

        return redirect("restaurant_detail", restaurant_id=restaurant.id)

    return redirect("restaurant_detail", restaurant_id=restaurant.id)
# =========================
# REGISTER
# =========================
def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created!")
            return redirect("login")
    else:
        form = UserCreationForm()

    return render(request, "register.html", {"form": form})


# =========================
# LOGIN
# =========================
def login_view(request):
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            messages.success(request, "Giriş başarılı!")
            return redirect("home")
    else:
        form = AuthenticationForm()

    return render(request, "login.html", {"form": form})


# =========================
# LOGOUT
# =========================
def logout_view(request):
    logout(request)
    messages.info(request, "Çıkış yapıldı.")
    return redirect("home")


# =========================
# STATIC
# =========================
def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")

# =========================
# DELETE REVIEW
# =========================
@login_required
def delete_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)

    # sadece yorumu yazan kişi silebilir
    if review.user != request.user:
        messages.error(request, "You cannot delete this review.")
        return redirect("restaurant_detail", restaurant_id=review.restaurant.id)

    review.delete()
    messages.success(request, "Review deleted.")

    return redirect("restaurant_detail", restaurant_id=review.restaurant.id)