from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Restaurant, Favorite


# =========================
# HOME
# =========================
def home(request):
    restaurants = Restaurant.objects.all()[:6]
    return render(request, "home.html", {"restaurants": restaurants})


# =========================
# READ - LIST
# =========================
def restaurant_list(request):
    restaurants = Restaurant.objects.all()
    return render(request, "restaurant_list.html", {"restaurants": restaurants})


# =========================
# READ - DETAIL
# =========================
def restaurant_detail(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)

    is_favorite = False
    if request.user.is_authenticated:
        is_favorite = Favorite.objects.filter(
            user=request.user,
            restaurant=restaurant
        ).exists()

    return render(request, "restaurant_detail.html", {
        "restaurant": restaurant,
        "is_favorite": is_favorite
    })


# =========================
# CREATE
# =========================
@login_required
def restaurant_create(request):
    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")

        Restaurant.objects.create(
            name=name,
            description=description
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
        return redirect("restaurant_detail", restaurant.id)

    return render(request, "restaurant_form.html", {
        "restaurant": restaurant
    })


# =========================
# DELETE
# =========================
@login_required
def restaurant_delete(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)

    if request.method == "POST":
        restaurant.delete()
        messages.success(request, "Restaurant deleted!")
        return redirect("restaurant_list")

    return render(request, "restaurant_confirm_delete.html", {
        "restaurant": restaurant
    })


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
# STATIC PAGES
# =========================
def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")