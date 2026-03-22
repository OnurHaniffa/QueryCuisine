from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Restaurant, Review
from .forms import ReviewForm

def home(request):
    restaurants = Restaurant.objects.all()
    return render(request, "home.html", {"restaurants": restaurants})


@login_required
def restaurant_detail(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)
    reviews = restaurant.reviews.all()
    form = ReviewForm()

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