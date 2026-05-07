# QueryCuisine

Restaurant review site we built for CSE 220 (Web Programming) at Acibadem University, Spring 2026. Think tiny Yelp, but Django.

The assignment calls the project FlavorMap. We picked QueryCuisine as our brand because it sounded better to us. Same project either way.

## What it does

You can browse restaurants, search by name, filter by category, location and price range, and sort by rating, popularity, newest or cheapest. Click into one and you get the photo, opening hours, menu, and the reviews other users left. Logged in users can leave a 1–5 star review (one per restaurant), reply to other peoples reviews, save favorites, and add their own restaurants with a photo upload. Each owner can add menu items and edit or delete only the things they made.

Theres also a profile page with your bio, your reviews, your favorites and the restaurants you added. Auth is the default Django stuff — register, login, logout — nothing custom.

Full feature list:

- Restaurant CRUD (with ownership checks, only the creator can edit/delete)
- Category, location and price filters (they stack)
- Search by restaurant name
- Sort: top rated / most reviewed / newest / cheapest
- 1–5 star reviews, one per user per restaurant
- Replies on reviews (one level)
- Menu CRUD per restaurant
- Favorites + favorites page
- Photo upload (Pillow)
- Opening hours Mon–Sun
- Register / login / logout
- Profile page with bio, my reviews, my favorites, my restaurants
- Average rating computed from real reviews
- Home page with Top Rated and Just Added sections
- Atomic transactions on the multi-step writes

Bonus stuff we did:

- Bootstrap 5 with a warm theme (maroon, forest green, cream) so it doesnt look like every other student project
- Combined multi-filter — search, category, location, price and sort all work together at the same time

## Stack

- Python 3.13 (3.10+ should be fine)
- Django 6.0.3
- SQLite (so no extra DB setup)
- Bootstrap 5 + Bootstrap Icons via CDN
- Pillow for the photo uploads

## Running it locally

```bash
git clone https://github.com/OnurHaniffa/QueryCuisine.git
cd QueryCuisine

python3 -m venv venv
source venv/bin/activate          # windows: venv\Scripts\activate

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Then open http://127.0.0.1:8000/ in the browser.

If you want to use the admin panel, make a superuser first:

```bash
python manage.py createsuperuser
```

Admin lives at `/admin/`.

## One thing that bit us a few times

When you pull new code, run `python manage.py migrate` again. If a teammate changed a model and you skip this step, half the pages crash with "no such table" and you will spend 20 minutes wondering why. Just run it.

## Team

- Onur Mohamed Haniffa
- Berfin Güneri — 231401058
- Ada Ağaçhan
- Hatice Sudenaz Acar — 231401044

CSE 220 — Web Programming, Spring 2026
Acibadem Mehmet Ali Aydınlar University
Instructor: Ahmet Bulut
