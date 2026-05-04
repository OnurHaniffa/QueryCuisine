# QueryCuisine — Complete Project Plan

## CSE 220 Web Programming | Spring 2026 | Acıbadem University

**Team Size:** 4 people
**Current Week:** ~14 (April 30, 2026) — **FINAL STRETCH**
**Progress Demo:** Week 8 ✅ DONE
**Final Demo:** Weeks 14-15 (next week — this is what we're sprinting to)

---

# 🚨 FINAL STRETCH HANDOFF — START HERE 🚨

> **For teammates joining the final push:** read this section first, then jump to Week 9 and Weeks 10-11. Earlier weeks (5-8) are kept as reference but are already done.

## Where the project stands today (May 4, 2026)

**🎉 ALL 16 MANDATORY FEATURES ARE NOW IMPLEMENTED.** Browser-tested end-to-end. Zero 500s on any route. The remaining work is final-demo prep + the hardcopy report.

**✅ Foundation (done since Week 6):**
- Django project + `restaurants` app, `INSTALLED_APPS` configured
- All 9 models created and migrated (`Category`, `Location`, `Restaurant`, `OpeningHours`, `MenuItem`, `Review`, `ReviewReply`, `Favorite`, `UserProfile`)
- Admin panel customized for every model
- Test data: 6 restaurants, 24 menu items, 18 reviews, 28 opening hours entries
- Bootstrap 5 + Bootstrap Icons + warm color theme (maroon / green / cream)
- Progress Demo (Week 8) delivered

**✅ Mandatory features — every one of the 16:**

| # | Feature | Where it lives |
|---|---|---|
| 1 | Restaurant CRUD with ownership checks | `restaurant_create` / `restaurant_update` / `restaurant_delete` views + `restaurant_form.html` + `restaurant_confirm_delete.html` |
| 2 | Category filter | `restaurant_list` view, `?category=N` query param |
| 3 | Location filter | same view, `?location=N` |
| 4 | Price filter | same view, `?price=€` / `€€` / `€€€` |
| 5 | Reviews & ratings | `add_review` / `delete_review` views + form on `restaurant_detail.html` |
| 6 | Average rating per restaurant | `Restaurant.average_rating()` method, displayed on cards + detail |
| 7 | Search by name | `?q=...` on the list page |
| 8 | User auth | `register_view` / `login_view` / `logout_view`, `RegisterForm` with email, auto-login, `UserProfile` auto-created |
| 9 | Menu CRUD with ownership checks | `menu_item_create` / `menu_item_update` / `menu_item_delete` views + `menu_item_form.html` + `menu_item_confirm_delete.html` |
| 10 | Favorites | `toggle_favorite` view + `/favorites/` list page (`favorites.html`) |
| 11 | Photo upload working end-to-end | `MEDIA` config + `RestaurantForm` with `photo` + `enctype="multipart/form-data"` on the form template |
| 12 | Opening hours display | `restaurant_detail.html` "Opening Hours" card |
| 13 | Popular ranking / sort | `?sort=rating` (Top Rated, via `Avg`), `?sort=popular` (most reviewed, via `Count`), `?sort=newest`, `?sort=cheap` |
| 14 | User profile page | `profile_view` + `profile.html` — bio editor, my reviews, my favorites, my restaurants |
| 15 | Review replies (one level) | `add_reply` / `delete_reply` views + reply form on `restaurant_detail.html` |
| 16 | Atomic transactions | `@transaction.atomic` on `restaurant_create` |

**✅ Bonus / polish on top:**
- Django messages framework rendered as Bootstrap alerts on every page
- Auth-aware navbar (Profile + Favorites links visible only when logged in)
- Already-logged-in users bounce away from `/login/` and `/register/`
- Photo placeholder when a restaurant has no `photo` uploaded
- Reusable `_restaurant_card.html` partial used by home page
- Owner-only Edit / Delete / "Add Menu Item" buttons via `{% if user == restaurant.created_by %}`
- Empty-state messages on every list page
- Cancel buttons on every form

**❌ Still left for the demo:**
- Final demo script practice (everyone, ~Week 14)
- 6-8 page hardcopy report (everyone, ~Week 14-15) — see "WEEK 14-15 — Final Demo + Report" below

## How we got here (May 4, 2026)

The team split across Week 9 / Weeks 10-11 didn't go cleanly. Adaag landed broken Restaurant CRUD on May 1; Berfin's May 4 commit fixed filters/search/sort and added the favorites + add_review views, but Restaurant CRUD was still 500ing on every endpoint and several other regressions remained. Onur did a recovery pass on May 4 (afternoon) that:

1. Cleaned up the nested `flavormap/` folder and the orphan project-root `templates/` folder
2. Fixed all 5 `TemplateDoesNotExist` 500s by creating the missing templates and renaming where needed
3. Plugged `RestaurantForm` into create/update (the views were bypassing it)
4. Added ownership checks to every owner-only operation (edit/delete restaurant, edit/delete menu item)
5. Restored the auth polish that got lost (auto-login, `UserProfile` auto-create, `RegisterForm` with email)
6. Made the detail page extend `base.html` properly (it was a standalone HTML doc with no navbar)
7. Built Menu CRUD, the User Profile page, and Review Replies UI from scratch
8. Wrapped `restaurant_create` in `@transaction.atomic` (mandatory feature 16)
9. Fixed the favorites page (template was looping the wrong variable)
10. Translated the Turkish flash messages to English for consistency

Browser-tested end-to-end with curl + Playwright. Every route 200 or proper redirect. No exceptions in the server log.

> **Note on Opening Hours:** Public CRUD for opening hours has been **dropped** from the worklist. The mandatory feature is "Opening hours **display**," which is already done on the restaurant detail page. Admins can add/edit hours through the Django admin panel. No public form needed.

### Weeks 12-13 — bonus + polish

Whoever finishes their slice first picks up bonus features. Priority order:
1. CSS polish + responsiveness — already mostly done, just sweep every page
2. JavaScript: star-rating widget + AJAX favorite toggle (no page reload)
3. Pagination on the restaurant list
4. Advanced multi-filter (combine search + filters cleanly)
5. Review likes/dislikes
6. Map iframe on restaurant detail

### Weeks 14-15 — final demo + report

Everyone helps. See "WEEK 14-15 — Final Demo + Report" section below for demo script and 6-8 page report template.

## Codebase conventions (READ BEFORE WRITING CODE)

These are how the existing code is set up. Match these so we don't end up with a Frankenstein.

| Convention | Value | Why |
|---|---|---|
| **View style** | Function-based views (FBV) only | This is what the course teaches. No CBVs. |
| **Auth** | Django built-in `django.contrib.auth` | No custom user model. |
| **Database** | SQLite (`db.sqlite3` in project root) | No Postgres / MySQL. |
| **URL parameter for restaurant routes** | `<int:restaurant_id>` everywhere | Single convention across the codebase. |
| **URL parameter for menu item routes** | `<int:menu_item_id>` | Same idea, named after the model. |
| **URL parameter for review / reply routes** | `<int:review_id>` / `<int:reply_id>` | Same. |
| **Template location** | Flat in `restaurants/templates/` (NO subfolder) | Existing templates are flat. Do not create `restaurants/templates/restaurants/`. |
| **Template render call** | `render(request, "yourfile.html", context)` | Path is relative to `restaurants/templates/`. |
| **Form classes** | All in `restaurants/forms.py` | One central file. |
| **Static assets** | Bootstrap 5 + Bootstrap Icons via CDN, custom CSS in `<style>` block in `base.html` | Already wired. |
| **Permission check pattern** | `if obj.created_by != request.user: return redirect(...)` inside view, plus `{% if user == obj.created_by %}` in template | Show edit/delete only to the owner. |
| **Commit style** | Descriptive, human-sounding, no Claude / AI attribution | "Add login view + register form" not "feat(auth)". |

## Daily git workflow for the final stretch

Everyone is working in parallel. Avoid stomping each other:

1. `git pull` before you start
2. Work on **your assigned slice only** — don't touch someone else's files
3. Test locally: `python manage.py runserver` and click through your feature
4. `git add <only your files>` — don't `git add .` blindly (could drag in someone's WIP)
5. Commit with a clear message
6. `git pull --rebase` then `git push`
7. If you hit a merge conflict in `views.py`, `urls.py`, or `forms.py`, ping Onur in the group chat — these are the high-traffic files

## Setup if you're catching up on a fresh machine

```bash
git clone <repo-url>
cd flavormap
python3 -m venv venv
source venv/bin/activate            # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser    # for admin panel access
python manage.py runserver
```

Open http://127.0.0.1:8000 — you should see the home page with restaurants listed.

---

# PART 1: Django 101 — What You Need to Know

## 1.1 What Is Django?

Django is a Python web framework. It follows the **MVT pattern**:

| Letter | Stands For | What It Does | File |
|--------|-----------|--------------|------|
| **M** | Model | Defines your database tables as Python classes | `models.py` |
| **V** | View | The logic — receives a request, does stuff, returns a response | `views.py` |
| **T** | Template | The HTML files with special tags for dynamic content | `templates/*.html` |

**How a request flows through Django:**

```
User clicks a link
       ↓
Browser sends request to: /restaurants/5/
       ↓
Django checks urls.py → finds matching pattern → calls the right view function
       ↓
View function in views.py:
  - Queries the database using Models
  - Prepares data (context dictionary)
  - Passes data to a Template
       ↓
Template (HTML file) renders with the data
       ↓
Django sends the HTML back to the browser
       ↓
User sees the page
```

## 1.2 Project vs App

Django has two levels of organization:

- **Project** = the whole website (settings, main URL config). Created once.
- **App** = a module within the project (restaurants, reviews, users). You can have multiple apps.

For QueryCuisine, we'll keep it simple: **one project, one app**.

```
QueryCuisine/                  ← Project root (Git repo lives here)
├── manage.py               ← Command-line tool (run server, migrations, etc.)
├── QueryCuisine/              ← Project settings folder (same name, confusing but normal)
│   ├── __init__.py
│   ├── settings.py         ← Database config, installed apps, templates config
│   ├── urls.py             ← Main URL router (delegates to app URLs)
│   ├── wsgi.py             ← Deployment (ignore for now)
│   └── asgi.py             ← Deployment (ignore for now)
├── restaurants/            ← Your main app (all your code goes here)
│   ├── __init__.py
│   ├── models.py           ← Database models (Restaurant, Review, etc.)
│   ├── views.py            ← View functions (logic)
│   ├── urls.py             ← App-level URL patterns (you create this)
│   ├── forms.py            ← Form classes (you create this in MS3)
│   ├── admin.py            ← Admin panel registration
│   ├── apps.py             ← App config (auto-generated, rarely touch)
│   ├── tests.py            ← Tests (optional for this project)
│   └── templates/          ← HTML templates (you create this folder)
│       └── restaurants/
│           ├── base.html
│           ├── home.html
│           ├── restaurant_list.html
│           └── ...
├── static/                 ← CSS, JS, images
├── media/                  ← User-uploaded files (photos)
├── requirements.txt        ← Python dependencies
├── .gitignore
└── README.md
```

## 1.3 Key Files Explained

### `settings.py` — The Brain
Controls everything: which apps are installed, where templates live, database config, static files, etc. You'll edit this several times throughout the project.

### `urls.py` — The Router
Maps URLs to view functions. Think of it like a phone switchboard:
- Someone calls `/restaurants/` → connect them to `restaurant_list` view
- Someone calls `/restaurants/5/` → connect them to `restaurant_detail` view with id=5

### `models.py` — The Database
Each class = a database table. Each attribute = a column. Django converts these to SQL automatically.

### `views.py` — The Logic
Functions that receive an HTTP request and return an HTTP response. They're the middleman between URLs and templates.

### `templates/` — The HTML
HTML files with Django template tags (`{{ variable }}`, `{% for %}`, `{% if %}`). Django fills in the data before sending to the browser.

## 1.4 The Migration System

When you change `models.py`, you need to tell Django to update the database:

```bash
python manage.py makemigrations    # Step 1: Django generates a migration file (the plan)
python manage.py migrate           # Step 2: Django executes the plan on the database
```

**Always do both steps after changing models.** If you forget, your code will reference columns that don't exist in the database yet.

---

# PART 2: Environment & Git Setup

## 2.1 Initial Setup (Person Who Creates the Repo)

### Step 1: Create project folder and virtual environment

```bash
cd ~/Projects
mkdir QueryCuisine
cd QueryCuisine

# Create a virtual environment (isolated Python for this project)
python3 -m venv venv

# Activate it (you'll do this every time you open terminal to work on the project)
source venv/bin/activate

# Your terminal prompt should now show (venv) at the beginning
```

**What is a virtual environment?**
It's a sandboxed Python installation just for this project. When you `pip install django`, it only installs inside this sandbox — not globally on your machine. This prevents version conflicts between projects.

### Step 2: Install Django and Pillow

```bash
pip install django pillow

# Pillow is needed for ImageField (restaurant photos)
# Save the exact versions so teammates install the same thing
pip freeze > requirements.txt
```

### Step 3: Create the Django project and app

```bash
# Create the project (note the dot at the end — it means "in current directory")
django-admin startproject QueryCuisine .

# Create the main app
python manage.py startapp restaurants
```

### Step 4: Register the app in settings.py

Open `QueryCuisine/settings.py` and find `INSTALLED_APPS`. Add your app:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'restaurants',  # ← Add this line
]
```

**Why?** Django doesn't know your app exists until you register it. Without this, models won't be detected, templates won't be found, etc.

### Step 5: Verify it works

```bash
python manage.py runserver
```

Open your browser to `http://127.0.0.1:8000/` — you should see the Django rocket page. Press `Ctrl+C` to stop the server.

## 2.2 Git Setup

### Step 1: Create .gitignore

Create a file called `.gitignore` in the project root (`~/Projects/QueryCuisine/`):

```gitignore
# Python
__pycache__/
*.pyc
*.pyo

# Virtual environment
venv/

# Django
db.sqlite3
db.sqlite3-journal

# Media uploads
media/

# IDE files
.idea/
.vscode/
*.swp
*.swo

# OS files
.DS_Store
Thumbs.db

# Environment variables
.env
```

**Why each one:**
- `venv/` — huge folder, each person creates their own
- `db.sqlite3` — each person has their own local database
- `media/` — uploaded files, too large for Git
- `.idea/` / `.vscode/` — IDE settings are personal, don't share
- `.DS_Store` — macOS junk files

### Step 2: Initialize Git and first commit

```bash
cd ~/Projects/QueryCuisine
git init
git add .
git commit -m "Initial Django project setup with restaurants app"
```

### Step 3: Create GitHub repo and push

1. Go to GitHub → New Repository
2. Name: `QueryCuisine`
3. **Do NOT** check "Add README" or ".gitignore" (we already have them)
4. Create repository
5. Follow the "push an existing repository" commands:

```bash
git remote add origin https://github.com/YOUR-USERNAME/QueryCuisine.git
git branch -M main
git push -u origin main
```

### Step 4: Add teammates as collaborators

GitHub → Your repo → Settings → Collaborators → Add people → Enter their GitHub usernames

## 2.3 Teammate Setup (Everyone Else)

Each teammate does this once:

```bash
cd ~/Projects   # or wherever they keep projects

# Clone the repo
git clone https://github.com/YOUR-USERNAME/QueryCuisine.git
cd QueryCuisine

# Create their own virtual environment
python3 -m venv venv
source venv/bin/activate

# Install the same packages
pip install -r requirements.txt

# Run migrations to create a local database
python manage.py migrate

# Verify it works
python manage.py runserver
```

## 2.4 Daily Git Workflow

**Before you start working:**
```bash
cd ~/Projects/QueryCuisine
source venv/bin/activate    # Activate virtual environment
git pull                    # Get latest code from teammates
```

**When you're done working:**
```bash
git add views.py templates/restaurants/home.html    # Add specific files you changed
git commit -m "added restaurant list view and template"
git push
```

**Golden rules:**
1. **Always pull before you start** — otherwise you'll get merge conflicts
2. **Commit often with clear messages** — "fixed stuff" is bad, "added category filter to restaurant list" is good
3. **Never commit `venv/`, `db.sqlite3`, or `.DS_Store`** — the `.gitignore` handles this if set up correctly
4. **If you get a merge conflict** — don't panic. Git marks the conflicting lines. Pick the right version, remove the markers, commit.

---

# PART 3: Week-by-Week Implementation Guide

---

## WEEK 5 — MS1: Project Skeleton + Static Pages

> **✅ DONE — kept here for reference only.** Skip this section if you're catching up. Skeleton, static pages, base template, URL patterns and view stubs all exist in the repo.

### Goal
Get the Django project running with 5+ URL routes, template inheritance, and hardcoded data displayed on pages. No database yet.

### Suggested Team Split
- **2 people:** Project setup + URL routing + views (the Python side)
- **2 people:** Templates + HTML structure (the frontend side)

Work together in the same room if possible — this first week is about everyone understanding the structure.

### Step 1: Configure Templates Directory

**What:** You're telling Django WHERE to find your HTML template files by editing `settings.py` and creating the folder structure.

**Why:** Django doesn't automatically know where your templates live. By default it only looks inside each app's `templates/` folder (because of `APP_DIRS: True`), but we also want a project-level templates directory for shared templates. Without this config, Django can't find any of your HTML files.

**Without this:** Every time you try to load a page, you'll get a `TemplateDoesNotExist` error — Django literally doesn't know where to look.

**Example:** When your view says `render(request, 'restaurants/home.html', context)`, Django searches every directory listed in `DIRS` plus every app's `templates/` folder. If `DIRS` is empty and the file isn't in the app folder, it fails.

In `QueryCuisine/settings.py`, find the `TEMPLATES` setting and update `DIRS`:

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # ← Change this line
        'APP_DIRS': True,
        # ... rest stays the same
    },
]
```

**What's happening here:**
- `BASE_DIR` = your project root folder (where `manage.py` lives)
- `BASE_DIR / 'templates'` = a folder called `templates` in your project root
- `APP_DIRS: True` = also look in each app's `templates/` folder (we'll use both)

Then create the template folders:

```bash
mkdir -p templates/restaurants
```

**Why `templates/restaurants/` and not just `templates/`?** This is called **template namespacing**. If you had multiple apps (e.g., `restaurants` and `blog`), both might have a `home.html`. Putting them in subfolders (`restaurants/home.html` vs `blog/home.html`) prevents name collisions.

---

### Step 2: Create the Base Template

**What:** You're creating a master HTML layout (`base.html`) that defines the common structure every page shares — the nav bar, footer, CSS links, and a "hole" where each page inserts its unique content.

**Why:** Without a base template, you'd copy-paste the same nav bar, footer, and `<head>` section into every single HTML file. If you wanted to change the nav bar later, you'd have to edit 10+ files. Template inheritance solves this — change the nav in one place, it updates everywhere.

**Without this:** Massive code duplication. Change the nav bar? Edit every file. Add a CSS file? Edit every file. Nightmare.

**Example:** Think of it like a picture frame. The frame (nav, footer, `<head>`) stays the same. Only the picture inside changes. Each page says "use this frame, but put THIS content in the middle."

**File: `templates/restaurants/base.html`**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}QueryCuisine{% endblock %}</title>
    <!-- You'll add Bootstrap CSS link here later -->
</head>
<body>
    <!-- Navigation Bar -->
    <nav>
        <a href="{% url 'home' %}">QueryCuisine</a>
        <a href="{% url 'restaurant_list' %}">Restaurants</a>
        <a href="{% url 'about' %}">About</a>
        <a href="{% url 'contact' %}">Contact</a>
        <!-- Later: login/logout links will go here -->
    </nav>

    <!-- Main Content — each page fills this block -->
    <main>
        {% block content %}
        {% endblock %}
    </main>

    <!-- Footer -->
    <footer>
        <p>&copy; 2026 QueryCuisine - Discover, Review, Share</p>
    </footer>
</body>
</html>
```

**Key concepts:**
- `{% block title %}QueryCuisine{% endblock %}` — defines a replaceable section. Child templates can override it.
- `{% url 'home' %}` — generates a URL by name (instead of hardcoding `/home/`). If you change the URL later, all links update automatically.
- `{% block content %}{% endblock %}` — the main "hole" that child templates fill.

### Step 3: Create Child Templates

**What:** You're creating the individual page HTML files (home, restaurant list, restaurant detail, about, contact). Each one "extends" the base template and only defines what's unique to that page.

**Why:** This is where template inheritance pays off. Instead of writing a full HTML document for every page, each child template says `{% extends "restaurants/base.html" %}` and only fills in the `{% block content %}` section. The nav, footer, and `<head>` come from `base.html` automatically.

**Without this:** You have no pages to display. The URL routes (Step 4) and views (Step 5) will have nothing to render, so every page would return an error.

**Example:** When Django renders `home.html`, it: (1) loads `base.html` as the skeleton, (2) finds `{% block content %}` in `home.html`, (3) plugs that content into the matching block in `base.html`, (4) returns the combined HTML. The user sees a full page with nav + home content + footer.

Each page extends `base.html` and only defines what's different.

**File: `templates/restaurants/home.html`**

```html
{% extends "restaurants/base.html" %}

{% block title %}QueryCuisine - Home{% endblock %}

{% block content %}
<h1>Welcome to QueryCuisine</h1>
<p>Discover the best restaurants near you.</p>

<!-- Top Rated Section (hardcoded for now, dynamic later) -->
<h2>Top Rated Restaurants</h2>
<!--
    Use a for loop to display restaurants passed from the view.
    Each restaurant is a dictionary with keys: name, category, rating, price_range

    Django template for loop syntax:
    {% for restaurant in top_restaurants %}
        <div>
            <h3>{{ restaurant.name }}</h3>
            <p>{{ restaurant.category }} | {{ restaurant.price_range }}</p>
            <p>Rating: {{ restaurant.rating }}/5</p>
        </div>
    {% empty %}
        <p>No restaurants yet.</p>
    {% endfor %}
-->

<!-- Newest Section (same pattern, use newest_restaurants variable) -->
<h2>Newest Additions</h2>
<!-- Same for loop pattern with newest_restaurants -->
{% endblock %}
```

**Create similar templates for:**

| Template File | What It Shows |
|---|---|
| `restaurant_list.html` | All restaurants in a grid/list. Loop through `restaurants` variable. Include a search bar (just the HTML for now). |
| `restaurant_detail.html` | Single restaurant's full info. Display `restaurant.name`, `.description`, `.address`, `.phone`, `.price_range`. Section for reviews (hardcoded). Section for menu items (hardcoded). |
| `about.html` | Static text about QueryCuisine. No dynamic data needed. |
| `contact.html` | Static contact form HTML (doesn't need to work yet). |

**Hint for `restaurant_detail.html`:** The view will pass a single `restaurant` dictionary. Access its fields with dot notation: `{{ restaurant.name }}`, `{{ restaurant.description }}`, etc. Also show hardcoded reviews list and menu items using `{% for %}` loops.

### Step 4: Create URL Patterns

**What:** You're creating the URL routing system — the mapping between URLs the user types in their browser and the Python functions that handle those requests. You'll create two files: the app-level URLs (`restaurants/urls.py`) and connect them to the project-level URLs (`QueryCuisine/urls.py`).

**Why:** Without URL patterns, Django has no idea what to do when someone visits `/restaurants/` or `/about/`. It would return a 404 error for everything except `/admin/`. URL patterns are the "phone switchboard" — they connect incoming calls (URLs) to the right handler (view function).

**Without this:** Every URL except `/admin/` returns "Page not found." Your views exist but nothing triggers them.

**Example:** When a user visits `http://127.0.0.1:8000/restaurants/3/`, Django: (1) checks `QueryCuisine/urls.py`, (2) sees `include('restaurants.urls')`, (3) checks `restaurants/urls.py`, (4) matches `restaurants/<int:pk>/` with `pk=3`, (5) calls `views.restaurant_detail(request, pk=3)`.

**File: `restaurants/urls.py`** (create this file — it doesn't exist yet)

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('restaurants/', views.restaurant_list, name='restaurant_list'),
    path('restaurants/<int:pk>/', views.restaurant_detail, name='restaurant_detail'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]
```

**Explanation:**
- `path('', ...)` — the homepage (root URL `/`)
- `path('restaurants/', ...)` — matches `/restaurants/`
- `path('restaurants/<int:pk>/', ...)` — matches `/restaurants/1/`, `/restaurants/2/`, etc. The `<int:pk>` captures the number and passes it to the view as a parameter called `pk`
- `name='home'` — gives the URL a name so you can reference it in templates with `{% url 'home' %}`

**File: `QueryCuisine/urls.py`** (edit the existing file to include your app's URLs)

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('restaurants.urls')),  # ← Delegates to your app's URLs
]
```

**Why `include()`?** It tells Django: "for any URL that doesn't start with `admin/`, go check `restaurants/urls.py` for a match." This keeps URL routing modular.

### Step 5: Create View Functions

**What:** You're writing the Python functions that handle each page request. Each view receives a request, prepares data, and returns an HTML response by rendering a template with that data. For now, the data is hardcoded dictionaries (fake data) — we'll replace it with real database queries in Week 6.

**Why:** Views are the "brain" of each page. URLs route the request TO the right function, but the function decides WHAT to show. Without views, URLs point to nothing. The view is where you'll eventually query the database, check if the user is logged in, process form submissions, etc.

**Without this:** All your URLs return `ViewDoesNotExist` errors. You have templates but nothing to feed data into them.

**Example:** When someone visits `/restaurants/`, Django calls `restaurant_list(request)`. That function creates a list of restaurant dictionaries, passes them to `restaurant_list.html` as `context`, and the template loops through them with `{% for restaurant in restaurants %}`. The user sees a page full of restaurants.

**Why hardcode data first?** It lets you build and test the entire frontend (templates, layout, for loops) WITHOUT dealing with database complexity yet. You can see exactly what the pages will look like. In Week 6, you swap the hardcoded dictionaries for `Restaurant.objects.all()` — the templates don't change at all because they use the same variable names.

**File: `restaurants/views.py`**

```python
from django.shortcuts import render

def home(request):
    # Hardcoded data — will be replaced with database queries in MS2
    top_restaurants = [
        {
            'id': 1,
            'name': 'Kebapçı Mehmet',
            'category': 'Turkish',
            'rating': 4.8,
            'price_range': '€€',
            'description': 'Authentic Turkish kebabs in the heart of Istanbul.',
        },
        {
            'id': 2,
            'name': 'Pasta La Vista',
            'category': 'Italian',
            'rating': 4.5,
            'price_range': '€€€',
            'description': 'Handmade pasta with imported Italian ingredients.',
        },
        # Add 2-3 more...
    ]

    newest_restaurants = [
        # Similar dictionaries for newest restaurants...
    ]

    # The context dictionary is what gets sent to the template
    # Keys become variable names in the template
    context = {
        'top_restaurants': top_restaurants,
        'newest_restaurants': newest_restaurants,
    }
    return render(request, 'restaurants/home.html', context)


def restaurant_list(request):
    # Hardcoded list of all restaurants
    restaurants = [
        # Same kind of dictionaries...
    ]
    context = {'restaurants': restaurants}
    return render(request, 'restaurants/restaurant_list.html', context)


def restaurant_detail(request, pk):
    # pk comes from the URL: /restaurants/1/ → pk=1
    # For now, hardcode a single restaurant
    # Later this will be: restaurant = Restaurant.objects.get(pk=pk)
    restaurant = {
        'id': pk,
        'name': 'Kebapçı Mehmet',
        'category': 'Turkish',
        'rating': 4.8,
        'price_range': '€€',
        'description': 'Authentic Turkish kebabs...',
        'address': 'Kadıköy, Istanbul',
        'phone': '+90 555 123 4567',
    }

    # Hardcoded reviews
    reviews = [
        {'user': 'Ali', 'rating': 5, 'comment': 'Best kebab in town!', 'date': '2026-02-15'},
        {'user': 'Ayşe', 'rating': 4, 'comment': 'Great food, slow service.', 'date': '2026-02-10'},
    ]

    # Hardcoded menu items
    menu_items = [
        {'name': 'Adana Kebab', 'description': 'Spicy minced meat kebab', 'price': 180, 'category': 'Main'},
        {'name': 'Ayran', 'description': 'Traditional yogurt drink', 'price': 30, 'category': 'Drink'},
    ]

    context = {
        'restaurant': restaurant,
        'reviews': reviews,
        'menu_items': menu_items,
    }
    return render(request, 'restaurants/restaurant_detail.html', context)


def about(request):
    return render(request, 'restaurants/about.html')


def contact(request):
    return render(request, 'restaurants/contact.html')
```

**Key concept:** The `render()` function takes three things:
1. The `request` object (always passed through)
2. The template path (relative to your templates directory)
3. The `context` dictionary (data the template can use)

### Step 6: Run and Test

**What:** You're starting Django's built-in development server and visiting every URL to confirm everything connects properly — URLs → views → templates → rendered HTML.

**Why:** This is your first "does it actually work?" moment. Catching errors now (typos in URLs, missing templates, wrong variable names) is easy. If you build 3 more features before testing, tracking down which change broke things becomes a nightmare.

**Without this:** You could have silent bugs lurking — a misspelled template path, a view that forgot to return a response, a URL pattern that doesn't match. These compound if not caught early.

**Example:** You visit `/restaurants/1/` and see a page with "Kebapçı Mehmet" and its reviews. This proves: (1) the URL pattern captured `pk=1` correctly, (2) the view built the context dictionary, (3) the template rendered the data with `{{ restaurant.name }}`, (4) template inheritance worked (you see the nav bar from `base.html`).

```bash
python manage.py runserver
```

Visit each URL and verify it works:
- `http://127.0.0.1:8000/` — Home page with top rated and newest
- `http://127.0.0.1:8000/restaurants/` — Restaurant list
- `http://127.0.0.1:8000/restaurants/1/` — Restaurant detail
- `http://127.0.0.1:8000/about/` — About page
- `http://127.0.0.1:8000/contact/` — Contact page

### Checkpoint — What Should Work
- [ ] All 5 URLs load without errors
- [ ] Navigation links work (clicking "Restaurants" goes to restaurant list)
- [ ] Home page shows hardcoded restaurant data via `{% for %}` loops
- [ ] Restaurant detail page shows restaurant info, reviews, menu items
- [ ] All pages share the same nav bar and footer (template inheritance)

### Git Commit
```bash
git add .
git commit -m "MS1: project skeleton with URL routing, views, and template inheritance"
git push
```

---

## WEEK 6 — MS2: Models + Admin + Dynamic Data

> **✅ MOSTLY DONE — kept here for reference only.** All 9 models, admin customization, sample data, and dynamic home/list/detail pages are live. ⚠️ **One leftover from this week:** Step 7 (MEDIA config) was never actually applied to `settings.py` — it's been moved into Person A's slice for Week 9. See the "STATUS" callout in Step 7 below.

### Goal
Replace all hardcoded data with real database models. Set up the admin panel. Populate with sample data. Share GitHub repo with TA.

### Suggested Team Split
- **Person A + B:** Define models in `models.py`, run migrations, register in admin
- **Person C + D:** Update views to query database, update templates if needed

### Step 1: Design and Create Models

**What:** You're defining Python classes in `models.py` that Django automatically converts into database tables. Each class = a table, each attribute = a column. You'll create 9 models: Category, Location, Restaurant, OpeningHours, MenuItem, Review, ReviewReply, Favorite, and UserProfile.

**Why:** Until now, all your restaurant data was hardcoded dictionaries in `views.py`. That's not a real application — you can't add restaurants, the data disappears when you restart, and there's no way for users to write reviews. Models give you a real database where data persists, can be queried, filtered, sorted, and related to each other.

**Without this:** Your app is just static HTML with fake data. No CRUD (create/read/update/delete), no user reviews, no search, no filtering — basically none of the assignment features work.

**Example:** When you define `class Restaurant(models.Model): name = models.CharField(max_length=200)`, Django generates SQL like `CREATE TABLE restaurants_restaurant (id INTEGER PRIMARY KEY, name VARCHAR(200), ...)`. Then in views, you can do `Restaurant.objects.filter(category__name='Turkish')` to get all Turkish restaurants — Django translates this to `SELECT * FROM restaurants_restaurant JOIN ... WHERE category.name = 'Turkish'`.

**File: `restaurants/models.py`**

This is the most important file in your project. Every model becomes a database table.

```python
from django.db import models
from django.contrib.auth.models import User

# ---------- CATEGORY ----------
# Simple model: just a name. Used as a foreign key on Restaurant.
# Fields: name (CharField), slug (SlugField — URL-friendly version of name)
#
# Example:
# class Category(models.Model):
#     name = models.CharField(max_length=100)
#     slug = models.SlugField(unique=True)
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name_plural = "categories"  # Fix admin showing "categorys"


# ---------- LOCATION ----------
# Represents a city/district. Restaurants are in a Location.
# Fields: city (CharField), district (CharField)
#
# The __str__ should return something like "Kadıköy, Istanbul"
# Use class Meta to set unique_together = ['city', 'district']
# so you can't have duplicate location entries.


# ---------- RESTAURANT ----------
# The main model. Has foreign keys to Category, Location, and User (creator).
#
# Fields you need:
#   name         → CharField(max_length=200)
#   description  → TextField
#   address      → CharField(max_length=300)
#   phone        → CharField(max_length=20)
#   price_range  → CharField with choices
#   category     → ForeignKey(Category)
#   location     → ForeignKey(Location)
#   created_by   → ForeignKey(User)  — who added this restaurant
#   photo        → ImageField(upload_to='restaurants/', blank=True, null=True)
#   created_at   → DateTimeField(auto_now_add=True)
#   updated_at   → DateTimeField(auto_now=True)
#
# For price_range, use Django's choices:
#
# PRICE_CHOICES = [
#     ('€', 'Budget'),
#     ('€€', 'Mid-Range'),
#     ('€€€', 'Fine Dining'),
# ]
# price_range = models.CharField(max_length=3, choices=PRICE_CHOICES)
#
# Add a method to compute average rating:
#
# def average_rating(self):
#     reviews = self.reviews.all()  # uses related_name from Review model
#     if reviews.exists():
#         return round(reviews.aggregate(models.Avg('rating'))['rating__avg'], 1)
#     return 0
#
# The aggregate() function runs a SQL AVG query — very efficient.
#
# __str__ should return the restaurant name.


# ---------- OPENING HOURS ----------
# One entry per restaurant per day.
# Fields: restaurant (FK), day_of_week (IntegerField with choices 0-6),
#         open_time (TimeField), close_time (TimeField)
#
# DAY_CHOICES = [
#     (0, 'Monday'), (1, 'Tuesday'), (2, 'Wednesday'),
#     (3, 'Thursday'), (4, 'Friday'), (5, 'Saturday'), (6, 'Sunday'),
# ]
#
# Use class Meta: unique_together = ['restaurant', 'day_of_week']
# so a restaurant can't have two Monday entries.
#
# Use ordering = ['day_of_week'] so they display in order.


# ---------- MENU ITEM ----------
# Belongs to a restaurant.
# Fields: restaurant (FK), name, description, price (DecimalField), category (CharField)
#
# For price, use: models.DecimalField(max_digits=8, decimal_places=2)
# This supports prices up to 999,999.99
#
# category here is a simple CharField (like "Main", "Appetizer", "Drink", "Dessert")
# — NOT a foreign key to Category model (that's for restaurant categories).


# ---------- REVIEW ----------
# A user's review of a restaurant. One review per user per restaurant.
#
# Fields:
#   restaurant  → ForeignKey(Restaurant, related_name='reviews')
#   user        → ForeignKey(User, related_name='reviews')
#   rating      → IntegerField with validators (MinValueValidator(1), MaxValueValidator(5))
#   comment     → TextField
#   created_at  → DateTimeField(auto_now_add=True)
#
# For the rating validators:
# from django.core.validators import MinValueValidator, MaxValueValidator
# rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
#
# class Meta:
#     unique_together = ['restaurant', 'user']  # One review per user per restaurant
#     ordering = ['-created_at']  # Newest first
#
# IMPORTANT: related_name='reviews' lets you do restaurant.reviews.all()
# Without it, you'd have to write restaurant.review_set.all() — less clean.


# ---------- REVIEW REPLY ----------
# One level of nesting. A reply to a review.
# Fields: review (FK), user (FK), text (TextField), created_at (DateTimeField)
#
# related_name='replies' on the review FK so you can do review.replies.all()


# ---------- FAVORITE ----------
# A many-to-many relationship between User and Restaurant.
# Fields: user (FK), restaurant (FK), added_at (DateTimeField)
#
# class Meta:
#     unique_together = ['user', 'restaurant']  # Can't favorite twice


# ---------- USER PROFILE ----------
# Extends the built-in User model with extra fields.
# Fields: user (OneToOneField to User), bio (TextField, blank=True)
#
# OneToOneField means each User has exactly one Profile and vice versa.
# Access it like: user.profile.bio
```

**After writing your models, run migrations:**

```bash
python manage.py makemigrations
python manage.py migrate
```

**If you get errors:** Read the error message carefully. Common issues:
- Forgot to import something (`from django.core.validators import ...`)
- Typo in field type (`CharFeld` instead of `CharField`)
- Missing `on_delete` parameter on ForeignKey (always use `on_delete=models.CASCADE`)

`on_delete=models.CASCADE` means: if the parent is deleted, delete the children too. E.g., if a restaurant is deleted, all its reviews are deleted. This is the most common choice.

### Step 2: Create a Superuser

**What:** You're creating an admin account — a special user with full access to Django's built-in admin panel, which lets you view, add, edit, and delete any data in your database through a web interface.

**Why:** The admin panel is Django's killer feature for development. Instead of writing SQL queries or building your own "add restaurant" form first, you can immediately start adding data through a polished admin interface. This is how you'll populate your database with sample restaurants, categories, reviews, etc. for the Week 8 demo.

**Without this:** You have no way to add data to your database (yet). Your models exist as empty tables. Your views query `Restaurant.objects.all()` and get back nothing. Every page shows "No restaurants yet."

**Example:** After creating a superuser with username `admin` and password `admin1234`, you visit `http://127.0.0.1:8000/admin/`, log in, click "Restaurants", click "Add Restaurant", fill in the form, and click Save. Now `Restaurant.objects.all()` returns that restaurant, and your pages show real data.

```bash
python manage.py createsuperuser
# Enter a username, email (optional), and password
# Remember these — you'll use them to log into the admin panel
```

### Step 3: Register Models in Admin

**What:** You're telling Django's admin panel which of your models to show and how to display them. By default, the admin doesn't know about your models — you have to register each one in `admin.py`. You'll also customize what columns appear in the list view, add search bars, and add filter sidebars.

**Why:** Without registration, your models are invisible in the admin panel. You'd see "Restaurants" in the sidebar but clicking it shows nothing — because the `Restaurant` model isn't registered. Registration also lets you customize the admin to be actually useful: seeing the restaurant name, category, and price at a glance instead of just "Restaurant object (1)".

**Without this:** You go to `/admin/` and see... nothing (or just "Users" and "Groups" from Django's built-in auth). No way to add restaurants, categories, reviews, or any of your custom data through the admin.

**Example:** With `list_display = ['name', 'category', 'location', 'price_range']`, the admin shows a table like:
| Name | Category | Location | Price Range |
|------|----------|----------|-------------|
| Kebapçı Mehmet | Turkish | Kadıköy, Istanbul | €€ |
| Trattoria Bella | Italian | Beşiktaş, Istanbul | €€€ |

Without `list_display`, you'd just see "Restaurant object (1)", "Restaurant object (2)" — useless.

**File: `restaurants/admin.py`**

```python
from django.contrib import admin
from .models import (
    Category, Location, Restaurant, OpeningHours,
    MenuItem, Review, ReviewReply, Favorite, UserProfile
)

# Basic registration — just makes the model visible in admin:
# admin.site.register(Category)

# Better: customize what columns show in the admin list view.
# Example for Restaurant:

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'location', 'price_range', 'created_by', 'created_at']
    list_filter = ['category', 'location', 'price_range']
    search_fields = ['name', 'description']
    # list_display = columns shown in the list
    # list_filter = filter sidebar on the right
    # search_fields = adds a search bar at the top

# Do similar customizations for:
# - Category: list_display = ['name', 'slug']
# - Location: list_display = ['city', 'district']
# - Review: list_display = ['restaurant', 'user', 'rating', 'created_at']
#           list_filter = ['rating']
# - MenuItem: list_display = ['name', 'restaurant', 'price', 'category']
#             list_filter = ['category']
# - OpeningHours: list_display = ['restaurant', 'day_of_week', 'open_time', 'close_time']

# For the simpler models (ReviewReply, Favorite, UserProfile),
# basic admin.site.register() is fine.
```

Visit `http://127.0.0.1:8000/admin/` and log in with your superuser credentials. You should see all your models.

### Step 4: Populate Sample Data

**What:** You're manually adding realistic test data to your database through the admin panel — categories, locations, restaurants, menu items, reviews, and opening hours.

**Why:** A database full of realistic data is what makes the difference between a demo that looks like a real product and one that looks empty and unfinished. Your Week 8 demo is judged on "does this app work with real data?" If your restaurant list shows one restaurant called "Test" with no reviews, no photo, and no menu — that's a bad impression. 10+ restaurants with varied categories, locations, realistic Turkish names, and actual reviews? That looks professional.

**Without this:** Every page shows "No restaurants yet" or empty lists. Your filters have nothing to filter. Your "Top Rated" section is blank. The demo falls flat because there's nothing to demonstrate.

**Example:** After adding data, your home page shows "Top Rated: Karadeniz Pide Salonu (4.8★), Trattoria Bella (4.5★)..." and "Newest: Taco Loco, Tokyo Ramen House...". Your category filter dropdown shows "Turkish (3), Italian (2), Seafood (1)". Your restaurant detail pages have 3-4 reviews each with different ratings. THIS is what impresses during the demo.

**Tip:** Later in Week 12, we'll create a `seed` management command that does this automatically with one terminal command. But for now, manual entry through admin helps you understand the data relationships firsthand.

Through the admin panel, add:
- **4-5 categories** (Turkish, Italian, Fast Food, Seafood, Cafe)
- **3-4 locations** (Istanbul/Kadıköy, Istanbul/Beşiktaş, Istanbul/Üsküdar, Ankara/Çankaya)
- **8-10 restaurants** spread across categories and locations
- **3-4 menu items per restaurant**
- **Opening hours for a few restaurants**
- **5-10 reviews** on different restaurants

This data is crucial for your Week 8 demo. Real data makes everything look complete.

### Step 5: Update Views to Query the Database

**What:** You're replacing the hardcoded dictionaries from Week 5 with real database queries using Django's ORM (Object-Relational Mapper). Instead of `top_restaurants = [{'name': 'Kebapçı Mehmet', ...}]`, you'll write `top_restaurants = Restaurant.objects.annotate(avg_rating=Avg('reviews__rating')).order_by('-avg_rating')[:5]`.

**Why:** This is the core transition from "static mockup" to "real application." Your templates already work with variables like `{{ restaurant.name }}` — they don't care whether that data came from a hardcoded dictionary or a database query. By swapping the data source in the views, your entire app becomes dynamic without changing a single line of HTML.

**Without this:** Your pages still show the same hardcoded data from Week 5. Adding a restaurant through the admin panel doesn't make it appear on the website. The admin and the website are disconnected — two separate worlds.

**Example:** Before (Week 5): The home page always shows "Kebapçı Mehmet" and "Pasta La Vista" because they're hardcoded. After (Week 6): The home page queries `Restaurant.objects.all()`, so when you add "Tokyo Ramen House" through admin, it immediately appears on the website. When a user writes a review and changes the average rating, "Top Rated" re-sorts automatically.

Replace all hardcoded dictionaries with real database queries.

**File: `restaurants/views.py`**

```python
from django.shortcuts import render, get_object_or_404
from .models import Restaurant, Category, Location

def home(request):
    # Replace hardcoded data with database queries
    #
    # Get top 5 restaurants by rating:
    # You can't sort by a method (average_rating) directly in a query.
    # Instead, use annotation:
    #
    # from django.db.models import Avg
    # top_restaurants = Restaurant.objects.annotate(
    #     avg_rating=Avg('reviews__rating')
    # ).order_by('-avg_rating')[:5]
    #
    # What this does:
    # - annotate() adds a computed column (avg_rating) to each restaurant
    # - Avg('reviews__rating') follows the FK from Restaurant → Review → rating
    # - order_by('-avg_rating') sorts descending (highest first)
    # - [:5] limits to 5 results (SQL LIMIT 5)
    #
    # Get 5 newest restaurants:
    # newest_restaurants = Restaurant.objects.order_by('-created_at')[:5]

    context = {
        'top_restaurants': top_restaurants,
        'newest_restaurants': newest_restaurants,
    }
    return render(request, 'restaurants/home.html', context)


def restaurant_list(request):
    # Start with all restaurants
    # restaurants = Restaurant.objects.all()
    #
    # Also pass categories, locations for filter dropdowns:
    # categories = Category.objects.all()
    # locations = Location.objects.all()

    context = {
        'restaurants': restaurants,
        'categories': categories,
        'locations': locations,
    }
    return render(request, 'restaurants/restaurant_list.html', context)


def restaurant_detail(request, pk):
    # get_object_or_404: fetches the restaurant or returns a 404 page
    # Much better than try/except — one line instead of five.
    #
    # restaurant = get_object_or_404(Restaurant, pk=pk)
    # reviews = restaurant.reviews.all()  # uses related_name
    # menu_items = restaurant.menu_items.all()  # uses related_name
    # opening_hours = restaurant.opening_hours.all()  # uses related_name

    context = {
        'restaurant': restaurant,
        'reviews': reviews,
        'menu_items': menu_items,
        'opening_hours': opening_hours,
    }
    return render(request, 'restaurants/restaurant_detail.html', context)

# about and contact views stay the same — they don't use the database
```

### Step 6: Update Templates for Real Data

**What:** You're making small tweaks to your templates so they work with real Django model objects instead of dictionaries. The main changes: adding links that use the database primary key (`pk`), calling model methods like `average_rating`, and using Django template filters like `|timesince`.

**Why:** Dictionaries and Django model objects are accessed slightly differently. With a dictionary you might use `restaurant['name']`, but Django templates use dot notation for both (`{{ restaurant.name }}`), so MOST of your templates work without changes. The key difference is linking to detail pages — you need the real `pk` from the database, and you can now call model methods like `average_rating()` that compute values on the fly.

**Without this:** Links to restaurant detail pages break (the hardcoded `id` field doesn't exist on model objects — it's `pk`). Average ratings don't display. Timestamps show raw datetime objects instead of "2 days ago."

**Example:** Before: `<a href="/restaurants/1/">Restaurant</a>` (hardcoded, always goes to restaurant 1). After: `<a href="{% url 'restaurant_detail' restaurant.pk %}">{{ restaurant.name }}</a>` (dynamic — each restaurant links to its own page using its real database ID).

Your templates should mostly work already if you used the right variable names. Key changes:

**In `restaurant_list.html`:** Link each restaurant to its detail page:
```html
<a href="{% url 'restaurant_detail' restaurant.pk %}">{{ restaurant.name }}</a>
```

**In `restaurant_detail.html`:** Display the average rating:
```html
<p>Average Rating: {{ restaurant.average_rating }}/5</p>
```

Note: `restaurant.average_rating` calls the method you defined in the model. Django templates automatically call methods without parentheses.

### Step 7: Configure Media Files (for photos)

> **⚠️ STATUS: NOT YET DONE — moved to Week 9, owned by Person A (Onur).** This step was scheduled here originally but was skipped during MS2. The `Restaurant.photo` `ImageField` exists on the model but `MEDIA_URL` / `MEDIA_ROOT` are NOT in `settings.py`, so uploads currently won't save or serve. Person A will apply the snippet below as the very first thing in Week 9, before anyone touches photo upload or restaurant CRUD.

**What:** You're configuring Django to handle user-uploaded files (restaurant photos). This involves two settings (`MEDIA_URL` and `MEDIA_ROOT`) and adding a URL pattern so Django can serve these files during development.

**Why:** Django separates "static files" (your CSS, JS, logo — things YOU provide) from "media files" (things USERS upload — restaurant photos, profile pictures). Media files need their own storage location and URL path. Without this config, `ImageField` on your Restaurant model has nowhere to save files, and even if it did, Django wouldn't know how to serve them to the browser.

**Without this:** When someone uploads a restaurant photo, it either fails (no `MEDIA_ROOT`) or uploads but the `<img>` tag can't display it (no `MEDIA_URL` serving). You'd see broken image icons everywhere.

**Example:** After this config: a user uploads `kebab.jpg` → Django saves it to `media/restaurants/kebab.jpg` on disk → the template uses `{{ restaurant.photo.url }}` which outputs `/media/restaurants/kebab.jpg` → Django's dev server serves the file → the browser displays the image.

In `QueryCuisine/settings.py`, add at the bottom:

```python
import os

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

In `QueryCuisine/urls.py`, add media URL handling for development:

```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # ... your existing patterns ...
]

# Only in development — serves uploaded files
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

### Step 8: Share GitHub Repo with TA

**What:** You're adding your GitHub repository link to the shared class spreadsheet so your TA can access, review, and track your project's progress.

**Why:** This is a hard requirement — the assignment says "Share your GitHub repository on the shared spreadsheet by Week 6." The TA will review your commit history to verify all group members are contributing. If your repo isn't shared by this deadline, you risk losing marks.

**Without this:** The TA can't see your code, can't verify contributions, and you miss the MS2 deadline requirement. During the demo, the TA may reference your commit history — if they can't access it, that's a problem.

**Example:** Go to the shared Google Sheet (provided by your instructor), find your group row, and paste `https://github.com/YOUR-USERNAME/QueryCuisine`. Make sure the repo is **public** (easiest) or add the TA's GitHub username as a collaborator (Settings → Collaborators → Add people).

Add your GitHub repo link to the shared spreadsheet as instructed. Make sure the repo is either public or the TA is added as a collaborator.

### Checkpoint — What Should Work
- [ ] All models exist and migrations run clean
- [ ] Admin panel shows all models with custom list_display
- [ ] Database has sample data (restaurants, categories, reviews, etc.)
- [ ] Home page shows top-rated and newest restaurants from the database
- [ ] Restaurant list shows all restaurants from the database
- [ ] Restaurant detail shows real restaurant data, reviews, menu items
- [ ] Clicking a restaurant in the list goes to its detail page
- [ ] GitHub repo is shared with TA

### Git Commit
```bash
git add .
git commit -m "MS2: models, admin panel, dynamic views with database queries"
git push
```

---

## WEEK 7 — Polish + Demo Prep

> **✅ DONE — kept here for reference only.** Bootstrap 5, warm color theme, and Bootstrap Icons are wired in `base.html`.

### Goal
Make sure MS1 + MS2 are solid. Practice the demo. Fix bugs.

### Tasks
1. **Test every page** — click every link, check for errors
2. **Add more sample data** — the demo looks better with 10+ restaurants
3. **Write a demo script** — who presents what, in what order (see Week 8 section)
4. **Make sure everyone can run the project locally**
5. **Basic CSS** — even a little styling helps. Add Bootstrap via CDN to `base.html`:

```html
<!-- In <head> of base.html -->
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css"
      rel="stylesheet">

<!-- Before </body> -->
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js">
</script>
```

Then wrap your content in Bootstrap classes (`container`, `row`, `col`, `card`, `btn`, etc.). This single step transforms the whole look.

---

## WEEK 8 — Progress Demo

> **✅ DONE — Progress Demo delivered.** Kept here for reference.

### Demo Script (10 minutes)

| Time | What | Who |
|---|---|---|
| 0-2 min | Introduce QueryCuisine, explain the concept | Person A |
| 2-4 min | Show home page with top-rated/newest restaurants | Person B |
| 4-6 min | Show restaurant list → click into detail page → show reviews/menu | Person C |
| 6-8 min | Show admin panel, explain model design decisions | Person D |
| 8-10 min | Explain remaining features plan, Q&A | Everyone |

**Tips:**
- Run the server before the demo starts
- Have data already loaded (don't waste demo time adding data)
- Every person should be able to answer "how does the URL routing work?" or "explain your Restaurant model"

---

## WEEK 9 — MS3: Auth + CRUD + Reviews + Filtering

> **🔥 THIS IS WHERE THE FINAL STRETCH STARTS.** Read the "FINAL STRETCH HANDOFF" section at the very top of this file before you start writing code.
>
> **Order of operations matters this week:**
> 1. Person A ships **MEDIA config + Auth first** — everything else builds on auth.
> 2. Once auth is on `main`, Person B (Restaurant CRUD) and Person D (Search/Filter) unblock and can work in parallel.
> 3. Person C's review write-form is ALREADY DONE — they just add edit/delete review views + buttons.
>
> **Convention reminders before you start (full list at the top of this doc):**
> - Function-based views only — no class-based.
> - Templates are **flat** in `restaurants/templates/`. Do NOT create `restaurants/templates/restaurants/`. The plan snippets below sometimes show `restaurants/restaurant_detail.html` — translate that to just `detail.html` (or whatever the existing flat name is).
> - URL params: existing `restaurant_detail` keeps `<int:restaurant_id>`. NEW CRUD routes use `<int:pk>` (Django convention).
> - All forms go in `restaurants/forms.py` (already exists; currently has `ReviewForm`).

### Goal
Make QueryCuisine interactive. Users can register, log in, create/edit/delete restaurants and reviews, and filter results.

### Team Split
- **Person A — Onur:** **MEDIA config first** (Week 6 Step 7 leftover) → then **Authentication** (register, login, logout, `LOGIN_URL`, nav update)
- **Person B:** Restaurant CRUD (create, edit, delete forms with ownership check; photo upload works once Person A's MEDIA is in)
- **Person C:** Review system polish — **the review write-form is already done in `views.py` + `forms.py` + `detail.html`.** What's left: edit-review view, delete-review view, "Edit / Delete" buttons on each review (only visible to the review's author).
- **Person D:** Search and filtering (`?q=`, `?category=`, `?location=`, `?price=` on the restaurant list page)

### Authentication

**What:** You're adding user registration, login, and logout using Django's built-in authentication system. This includes creating a registration form, login/logout views, and updating the nav bar to show different options for logged-in vs. anonymous users.

**Why:** Almost every mandatory feature requires a logged-in user: writing reviews, creating restaurants, managing favorites, editing your own content. Without authentication, everyone is anonymous — there's no "my reviews," no "my favorites," no way to restrict who can edit or delete what. Auth is the foundation that the next 10+ features build on.

**Without this:** Anyone can delete any restaurant. Reviews have no author. Favorites don't work (favorites belong to a user). The entire concept of "ownership" doesn't exist. Your app is essentially a wiki where anyone can destroy anything.

**Example:** After implementing auth: (1) A new user visits `/register/`, fills in username/email/password, clicks Submit → account created, auto-logged in, redirected to home. (2) The nav bar now shows "Hello, ali" with a dropdown (Profile, Favorites, Logout) instead of "Login / Sign Up". (3) When Ali tries to visit `/restaurants/create/`, the `@login_required` decorator checks if they're logged in. If yes, show the form. If no, redirect to `/login/`. (4) When Ali writes a review, `review.user = request.user` automatically tags the review as Ali's.

Django has a built-in auth system. You don't build login from scratch.

**File: `restaurants/forms.py`** (create this file)

```python
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
```

**What's happening:** `UserCreationForm` is Django's built-in registration form. It already handles password validation, confirmation matching, etc. We're extending it to also ask for an email.

**Views for auth:**

```python
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from .forms import RegisterForm

def register_view(request):
    # If the request is POST → user submitted the form
    # If the request is GET → user is visiting the page (show empty form)
    #
    # POST flow:
    #   form = RegisterForm(request.POST)
    #   if form.is_valid():
    #       user = form.save()
    #       login(request, user)  # Auto-login after registration
    #       return redirect('home')
    #
    # GET flow:
    #   form = RegisterForm()
    #
    # Pass form to template in both cases.
    pass

def login_view(request):
    # Use Django's built-in AuthenticationForm
    # from django.contrib.auth.forms import AuthenticationForm
    #
    # POST flow:
    #   form = AuthenticationForm(request, data=request.POST)
    #   if form.is_valid():
    #       user = form.get_user()
    #       login(request, user)
    #       return redirect('home')
    #
    # GET flow:
    #   form = AuthenticationForm()
    pass

def logout_view(request):
    # logout(request)
    # return redirect('home')
    pass
```

**URLs to add:**
```python
path('register/', views.register_view, name='register'),
path('login/', views.login_view, name='login'),
path('logout/', views.logout_view, name='logout'),
```

**Template for register:** Create a form with `{{ form.as_p }}` which auto-renders all fields. Always include `{% csrf_token %}` inside the form (Django security requirement).

```html
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Register</button>
</form>
```

**Update `base.html` navigation:**
```html
{% if user.is_authenticated %}
    <span>Hello, {{ user.username }}</span>
    <a href="{% url 'logout' %}">Logout</a>
{% else %}
    <a href="{% url 'login' %}">Login</a>
    <a href="{% url 'register' %}">Register</a>
{% endif %}
```

### Restaurant CRUD

**What:** You're building the Create, Read, Update, Delete functionality for restaurants. Users can add new restaurants (Create), view them (Read — already done), edit their own restaurants (Update), and delete their own restaurants (Delete). You'll use Django's `ModelForm` to automatically generate forms from your model.

**Why:** This is the core "user-generated content" feature. Without CRUD, only the admin can add restaurants. With CRUD, any logged-in user can add their favorite restaurant, fix a typo in the description, or remove a listing. The assignment lists "Restaurant CRUD" as the first mandatory feature.

**Without this:** The only way to add restaurants is through the admin panel (`/admin/`). Regular users can browse but never contribute. The app is read-only for normal users.

**Example:** Ali logs in, clicks "Add Restaurant" in the nav, fills out the form (name: "Çiya Sofrası", category: Turkish, price: €€, address: "Kadıköy..."), uploads a photo, clicks Submit. The restaurant appears in the list immediately. Ali can later click "Edit" on his restaurant's detail page to update the phone number. Only Ali (the creator) sees the Edit/Delete buttons — other users don't, because the template checks `{% if user == restaurant.created_by %}`.

**Create a ModelForm for Restaurant:**

```python
# In forms.py
from .models import Restaurant

class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ['name', 'description', 'address', 'phone',
                  'price_range', 'category', 'location', 'photo']
        # Excludes: created_by (set automatically), created_at/updated_at (auto)
```

**Views for CRUD:**

```python
@login_required  # Redirects to login page if not logged in
def restaurant_create(request):
    # POST: form = RestaurantForm(request.POST, request.FILES)
    #   request.FILES is needed because of the photo ImageField
    #   if form.is_valid():
    #       restaurant = form.save(commit=False)  # Don't save to DB yet
    #       restaurant.created_by = request.user   # Set the creator
    #       restaurant.save()                      # Now save
    #       return redirect('restaurant_detail', pk=restaurant.pk)
    # GET: form = RestaurantForm()
    pass

@login_required
def restaurant_edit(request, pk):
    # restaurant = get_object_or_404(Restaurant, pk=pk)
    #
    # PERMISSION CHECK: only the creator can edit
    # if restaurant.created_by != request.user:
    #     return redirect('restaurant_detail', pk=pk)  # Or show 403
    #
    # POST: form = RestaurantForm(request.POST, request.FILES, instance=restaurant)
    #   The instance=restaurant makes the form pre-filled with existing data
    #   if form.is_valid(): form.save() and redirect
    # GET: form = RestaurantForm(instance=restaurant)
    pass

@login_required
def restaurant_delete(request, pk):
    # restaurant = get_object_or_404(Restaurant, pk=pk)
    #
    # PERMISSION CHECK: only the creator can delete
    # if restaurant.created_by != request.user:
    #     return redirect('restaurant_detail', pk=pk)
    #
    # Only accept POST (not GET) for deletion — security best practice
    # if request.method == 'POST':
    #     restaurant.delete()
    #     return redirect('restaurant_list')
    #
    # GET shows a confirmation page: "Are you sure you want to delete X?"
    pass
```

**URLs to add:**
```python
path('restaurants/create/', views.restaurant_create, name='restaurant_create'),
path('restaurants/<int:pk>/edit/', views.restaurant_edit, name='restaurant_edit'),
path('restaurants/<int:pk>/delete/', views.restaurant_delete, name='restaurant_delete'),
```

**Template hints:**
- Create form: `<form method="post" enctype="multipart/form-data">` — the `enctype` is needed for file uploads (photos)
- Delete confirmation: Show restaurant name, ask "Are you sure?", have a form with POST method and a "Delete" button
- Show form errors: `{% if form.errors %} {{ form.errors }} {% endif %}`

### Review System

> **✅ Write-form is already done.** `ReviewForm` in `forms.py` and the POST handling in `restaurant_detail` view + `detail.html` all work. One review per user is enforced.
>
> **What's left for Person C:**
> 1. `review_edit(request, pk)` view — pre-fill the existing review, save changes, redirect back to detail page. Permission check: only the review's author can edit.
> 2. `review_delete(request, pk)` view — POST-only, permission check, redirect back to detail page.
> 3. Two new URL patterns: `path('review/<int:pk>/edit/', ...)` and `path('review/<int:pk>/delete/', ...)`.
> 4. In `detail.html`, inside the `{% for review in reviews %}` loop: `{% if review.user == user %}` show "Edit" and "Delete" buttons.
> 5. A simple `review_edit.html` template (one form + submit).
>
> Skim the rest of this section for context, but skip the "ReviewForm" / POST-handler snippets — they're already in the codebase.

**What:** You're adding the ability for logged-in users to write reviews (1-5 stars + text comment) on restaurant detail pages. Each user can only review a restaurant once. Users can also edit or delete their own reviews.

**Why:** Reviews are the heart of QueryCuisine — it's a "Restaurant Review & Discovery Platform." Without reviews, there are no ratings, no average scores, no "Top Rated" section, no user-generated content. The review system also feeds into multiple other features: average rating calculation, user profiles ("my reviews"), review replies, and review likes (bonus).

**Without this:** Restaurants have no ratings. The "Top Rated" section on the homepage is empty. The `average_rating()` method returns 0 for every restaurant. There's nothing for users to read — the platform has no content beyond what the restaurant creator wrote.

**Example:** Ayşe visits Kebapçı Mehmet's detail page, scrolls to the review section, clicks 4 stars (the star widget highlights), types "Great food, slow service," clicks Submit. The page reloads showing her review at the top (newest first). The average rating updates from 4.8 to 4.6. If she tries to review again, she sees "You already reviewed this restaurant" instead of the form. She can click "Edit" on her review to change the rating, or "Delete" to remove it.

**ReviewForm:**
```python
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']
        # restaurant and user are set automatically in the view
```

**Add review submission to `restaurant_detail` view:**

```python
def restaurant_detail(request, pk):
    restaurant = get_object_or_404(Restaurant, pk=pk)
    reviews = restaurant.reviews.all()

    # Check if current user already reviewed this restaurant
    # user_review = None
    # if request.user.is_authenticated:
    #     user_review = Review.objects.filter(
    #         restaurant=restaurant, user=request.user
    #     ).first()

    # Handle review form submission
    # if request.method == 'POST' and request.user.is_authenticated:
    #     if user_review is None:  # Only if they haven't reviewed yet
    #         form = ReviewForm(request.POST)
    #         if form.is_valid():
    #             review = form.save(commit=False)
    #             review.restaurant = restaurant
    #             review.user = request.user
    #             review.save()
    #             return redirect('restaurant_detail', pk=pk)
    #     else:
    #         form = ReviewForm()  # Already reviewed
    # else:
    #     form = ReviewForm()

    context = {
        'restaurant': restaurant,
        'reviews': reviews,
        'form': form,
        'user_review': user_review,
    }
    return render(request, 'restaurants/restaurant_detail.html', context)
```

**Template hint:** Only show the review form if the user is logged in AND hasn't reviewed yet:
```html
{% if user.is_authenticated and not user_review %}
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Submit Review</button>
    </form>
{% elif user_review %}
    <p>You already reviewed this restaurant.</p>
{% else %}
    <p><a href="{% url 'login' %}">Log in</a> to write a review.</p>
{% endif %}
```

### Search & Filtering

**What:** You're adding a search bar and filter dropdowns (category, location, price range) to the restaurant list page. Users can search by name/description/location and narrow results using filters. All filters work via URL query parameters (`?q=kebab&category=1&price=€€`).

**Why:** With 20+ restaurants in the database, users need a way to find what they want. A user looking for "cheap Turkish food in Kadıköy" shouldn't have to scroll through every restaurant. Search + filtering makes the app actually usable. The assignment lists Search, Category System, Location Filter, and Price Range Filter as four separate mandatory features — this one step covers all four.

**Without this:** The restaurant list page dumps ALL restaurants on screen with no way to narrow results. Users have to scroll and scan manually. For 50+ restaurants, this is unusable. Also, you lose 4 mandatory feature checkboxes.

**Example:** A user types "pide" in the search bar → only "Karadeniz Pide Salonu" shows up (because `name__icontains='pide'` matches). They clear the search and select "Seafood" from the category dropdown + "Üsküdar" from location → only seafood restaurants in Üsküdar appear. They add price filter "€€€" → narrows further. The URL becomes `/restaurants/?category=4&location=3&price=€€€`. If nothing matches, they see "No restaurants found. Try adjusting your filters."

**Update `restaurant_list` view to handle query parameters:**

```python
def restaurant_list(request):
    restaurants = Restaurant.objects.all()

    # Search: check if 'q' parameter exists in the URL
    # Example URL: /restaurants/?q=kebab
    # query = request.GET.get('q', '')  # '' is default if not provided
    # if query:
    #     restaurants = restaurants.filter(
    #         Q(name__icontains=query) |
    #         Q(description__icontains=query) |
    #         Q(location__city__icontains=query)
    #     )
    # Note: Q objects allow OR logic. Import: from django.db.models import Q
    # icontains = case-insensitive "contains" (LIKE '%query%' in SQL)

    # Category filter: /restaurants/?category=1
    # category_id = request.GET.get('category', '')
    # if category_id:
    #     restaurants = restaurants.filter(category_id=category_id)

    # Location filter: /restaurants/?location=1
    # Same pattern as category

    # Price filter: /restaurants/?price=€€
    # Same pattern: restaurants = restaurants.filter(price_range=price)

    # Pass filter values back to template so dropdowns stay selected
    context = {
        'restaurants': restaurants,
        'categories': Category.objects.all(),
        'locations': Location.objects.all(),
        'query': query,
        'selected_category': category_id,
        'selected_location': location_id,
        'selected_price': price,
    }
    return render(request, 'restaurants/restaurant_list.html', context)
```

**Template filter form:**
```html
<form method="get">
    <input type="text" name="q" value="{{ query }}" placeholder="Search restaurants...">

    <select name="category">
        <option value="">All Categories</option>
        {% for cat in categories %}
            <option value="{{ cat.id }}"
                {% if selected_category == cat.id|slugify %}selected{% endif %}>
                {{ cat.name }}
            </option>
        {% endfor %}
    </select>

    <!-- Similar dropdowns for location and price -->

    <button type="submit">Filter</button>
</form>
```

**Why `method="get"` not `method="post"`?** Filters go in the URL (`?q=kebab&category=1`). This means users can bookmark filtered results and use the back button. Filters are reads, not writes — GET is correct.

### Checkpoint — What Should Work
- [ ] Users can register, log in, log out
- [ ] Nav bar shows different links for logged-in vs anonymous users
- [ ] Logged-in users can create a new restaurant
- [ ] Restaurant creator can edit and delete their restaurant
- [ ] Users can write one review per restaurant (1-5 stars + comment)
- [ ] Search bar filters restaurants by name/description/location
- [ ] Category, location, and price dropdowns filter correctly
- [ ] Empty results show "No restaurants found" message

---

## WEEKS 10-11 — Remaining Mandatory Features

### Team Split (rebalanced)
- **Person A — Onur:** Optional polish only (Onur's Week 9 Auth slice is already heavier because it unblocks everyone else). Picks up bonus features or pagination if time permits.
- **Person B:** **Menu CRUD** (reuses the Restaurant CRUD pattern they just built — should be ~30-45 min of pattern-copy) + **Favorites** system
- **Person C:** User Profile page + Review Replies
- **Person D:** Atomic Transactions + Popular Ranking/Sorting + Photo upload finalization

> **⚠️ Opening Hours CRUD has been DROPPED.** The mandatory requirement is "Opening hours display" which is already shipped on the detail page. Admins can edit hours via the admin panel — no public form needed. Don't build it.

### Menu Management

> **👤 Owned by Person B.** You already built Restaurant CRUD in Week 9 — Menu CRUD is the same pattern. Copy your `RestaurantForm` / `restaurant_create` / `restaurant_edit` / `restaurant_delete` and adapt for `MenuItem`. The big difference: menu items belong to a restaurant, so the create URL is nested (`restaurants/<int:pk>/menu/add/`) and the create view sets `menu_item.restaurant = restaurant` from the URL `pk` (same trick you use for `review.user = request.user`). Permission check: only the restaurant's `created_by` can add/edit/delete its menu items.

**What:** You're adding CRUD for menu items — restaurant owners can add, edit, and delete dishes (name, description, price, category like "Main", "Drink", "Dessert") that belong to their restaurant. The menu displays on the restaurant detail page.

**Why:** The assignment lists "Menu Management" as a mandatory feature. Menus are what users actually care about when deciding where to eat — "what do they serve and how much does it cost?" Without menus, the restaurant detail page is just a description and reviews, which isn't enough information for a user to decide.

**Without this:** Restaurant detail pages have no menu section. Users can see reviews but not what the restaurant serves or what it costs. You lose one mandatory feature checkbox.

**Example:** The owner of Kebapçı Mehmet goes to their restaurant detail page, sees a "Manage Menu" button (only visible to them), clicks "Add Item", fills in: Name: "Adana Kebab", Description: "Spicy minced meat kebab with charcoal grill", Price: 180 TL, Category: "Main". The item appears in the menu section immediately, organized by category with the price right-aligned.

Same CRUD pattern as Restaurant. Create `MenuItemForm`, add views for create/edit/delete, restrict to restaurant creator.

**Key difference:** Menu items belong to a restaurant, so the create URL should be nested:
```python
path('restaurants/<int:pk>/menu/add/', views.menu_item_create, name='menu_item_create'),
path('menu/<int:pk>/edit/', views.menu_item_edit, name='menu_item_edit'),
path('menu/<int:pk>/delete/', views.menu_item_delete, name='menu_item_delete'),
```

The create view receives the restaurant `pk` from the URL and sets `menu_item.restaurant` automatically (same pattern as `review.restaurant`).

### Favorites System

**What:** You're adding the ability for logged-in users to "favorite" (bookmark) restaurants and view their favorites list on a dedicated page. Clicking the heart button on a restaurant toggles it as a favorite. A separate `/favorites/` page shows all their saved restaurants.

**Why:** Favorites give users a personal connection to the platform — "my list of places I want to try." It's a mandatory feature and it's also one of the most demo-friendly features: during the final demo, you can show "register → browse → favorite a restaurant → go to favorites list → see it there." It demonstrates user-specific data.

**Without this:** There's no personalization. Every user sees the same thing. No "my saved restaurants." You lose one mandatory feature checkbox.

**Example:** Ayşe is browsing restaurants. She sees "Deniz Kızı Balık" and clicks the heart button (outline heart). It instantly fills in (red heart) and shows "Saved to Favorites" — without a page reload (AJAX). She favorites 3 more restaurants. Later, she clicks "Favorites" in the nav → sees her 4 saved restaurants in a grid. She clicks the heart on one to un-favorite it → it disappears from the list.

**Views:**

```python
@login_required
def toggle_favorite(request, pk):
    # restaurant = get_object_or_404(Restaurant, pk=pk)
    # favorite = Favorite.objects.filter(user=request.user, restaurant=restaurant)
    #
    # if favorite.exists():
    #     favorite.delete()  # Unlike
    # else:
    #     Favorite.objects.create(user=request.user, restaurant=restaurant)  # Like
    #
    # return redirect('restaurant_detail', pk=pk)
    pass

@login_required
def favorites_list(request):
    # favorites = Favorite.objects.filter(user=request.user).select_related('restaurant')
    # select_related reduces database queries by JOINing tables
    pass
```

**Template hint:** On the restaurant detail page, show a favorite/unfavorite button:
```html
{% if user.is_authenticated %}
    <form method="post" action="{% url 'toggle_favorite' restaurant.pk %}">
        {% csrf_token %}
        {% if is_favorited %}
            <button type="submit">Remove from Favorites</button>
        {% else %}
            <button type="submit">Add to Favorites</button>
        {% endif %}
    </form>
{% endif %}
```

Pass `is_favorited` from the view:
```python
is_favorited = Favorite.objects.filter(user=request.user, restaurant=restaurant).exists()
```

### User Profile

**What:** You're creating a profile page (`/profile/`) where logged-in users can see their bio, all their reviews, and all their favorited restaurants in one place. They can also edit their bio through a simple form.

**Why:** The profile page is a mandatory feature and it ties together everything the user has done on the platform. It's the "my account" page. Without it, users have no way to see their own activity — they'd have to visit each restaurant individually to find their reviews. It also gives the demo a natural flow: "Here's what Ali has reviewed and favorited."

**Without this:** Users have no central place to see their activity. "My reviews" and "my favorites" have no home. You lose one mandatory feature checkbox.

**Example:** Ali visits `/profile/` and sees: his username, email, bio ("Food lover based in Kadıköy"), then a "My Reviews" section showing 4 reviews he's written (with star ratings and restaurant names), and a "My Favorites" section showing 3 favorited restaurants as cards. He clicks "Edit Profile" to update his bio.

**View:**
```python
@login_required
def profile(request):
    # Get or create the UserProfile for the current user
    # profile, created = UserProfile.objects.get_or_create(user=request.user)
    # user_reviews = Review.objects.filter(user=request.user)
    # user_favorites = Favorite.objects.filter(user=request.user)
    #
    # Also handle profile edit (bio field) via a simple form
    pass
```

**Template shows:** Username, email, bio, list of their reviews, list of their favorites.

### Review Replies

**What:** You're adding the ability for users to reply to reviews (one level of nesting only — no replies to replies). Under each review, there's a small text input where any logged-in user can write a response.

**Why:** Review replies enable conversation — a restaurant owner can respond to criticism ("Sorry about the wait, we've hired more staff!"), or other users can agree/disagree with a review ("I had the same experience!" or "I think the reviewer went on a bad night"). It's a mandatory feature that adds social depth to the platform.

**Without this:** Reviews are one-way communication. If someone writes an unfair review, there's no way to respond. The review section feels static and isolated instead of conversational. You lose one mandatory feature checkbox.

**Example:** Mehmet (restaurant owner) sees a 2-star review on his restaurant: "Food was cold and waiter was rude." He clicks the reply input below it, types "We're sorry about your experience. We've addressed this with our staff and would love to have you back for a complimentary meal." The reply appears indented below the original review with Mehmet's name and timestamp.

**Add to `restaurant_detail` view** or create a separate view:

```python
@login_required
def reply_to_review(request, review_id):
    # review = get_object_or_404(Review, pk=review_id)
    # if request.method == 'POST':
    #     text = request.POST.get('text', '')
    #     if text:
    #         ReviewReply.objects.create(review=review, user=request.user, text=text)
    # return redirect('restaurant_detail', pk=review.restaurant.pk)
    pass
```

**Template:** Under each review, show existing replies and a small reply form:
```html
{% for review in reviews %}
    <div>
        <strong>{{ review.user.username }}</strong> — {{ review.rating }}/5
        <p>{{ review.comment }}</p>

        <!-- Replies -->
        {% for reply in review.replies.all %}
            <div style="margin-left: 40px;">
                <strong>{{ reply.user.username }}</strong>: {{ reply.text }}
            </div>
        {% endfor %}

        <!-- Reply form (one level only) -->
        {% if user.is_authenticated %}
            <form method="post" action="{% url 'reply_to_review' review.pk %}">
                {% csrf_token %}
                <input type="text" name="text" placeholder="Write a reply...">
                <button type="submit">Reply</button>
            </form>
        {% endif %}
    </div>
{% endfor %}
```

### Atomic Transactions

**What:** You're wrapping multi-step database operations in `transaction.atomic()` so they either ALL succeed or ALL roll back. If step 3 of 5 fails, steps 1 and 2 are undone — the database stays clean.

**Why:** This is a mandatory feature that demonstrates understanding of database integrity. Without transactions, you can end up with orphaned data. Example: creating a restaurant + its opening hours in one view. If the restaurant saves but the opening hours fail (maybe a validation error), you have a restaurant with no hours — half-created data that breaks your UI.

**Without this:** Database corruption from partial operations. A user registers but their profile creation fails → a User exists with no Profile → any code that accesses `user.profile` crashes. A restaurant is created but the photo upload fails → restaurant exists with a broken photo reference. You also lose one mandatory feature checkbox.

**Example:** A user creates a restaurant and adds 3 menu items in one form submission. With `transaction.atomic()`: if the restaurant saves fine but the third menu item has invalid data, ALL changes roll back — no restaurant, no menu items. The user sees an error message and can fix the issue. Without `atomic()`: the restaurant and 2 menu items are saved, the third fails silently, and you have incomplete data.

Use `transaction.atomic()` wherever you do multiple related database operations that must all succeed or all fail.

**Example — creating a restaurant with menu items in one go:**

```python
from django.db import transaction, IntegrityError

@login_required
def restaurant_create_with_menu(request):
    if request.method == 'POST':
        try:
            with transaction.atomic():
                # Save restaurant
                restaurant_form = RestaurantForm(request.POST, request.FILES)
                if restaurant_form.is_valid():
                    restaurant = restaurant_form.save(commit=False)
                    restaurant.created_by = request.user
                    restaurant.save()

                    # Save menu items (if submitted together)
                    # If any of these fail, the restaurant save is also rolled back
                    # ... process menu items ...
                else:
                    raise IntegrityError("Invalid form data")
        except IntegrityError:
            # Handle the error — show a message to the user
            pass
```

**Where else to use it:**
- Deleting a restaurant (cascading deletes of reviews, menu items, etc.)
- User registration + profile creation (both must succeed)
- Any view where you create/modify 2+ related objects

**Why?** Without `atomic()`, if step 2 fails after step 1 succeeded, you have orphaned data. With `atomic()`, everything rolls back to the state before the transaction started.

### Popular Ranking & Sorting

**What:** You're adding sort options to the restaurant list page (sort by: top rated, newest, price low→high, price high→low) and making the homepage show "Top Rated" and "Newest" sections dynamically from the database.

**Why:** This is a mandatory feature ("Popular Ranking"). Users need to discover the best restaurants quickly. Sorting by rating answers "where should I eat?" Sorting by newest answers "what just opened?" Sorting by price answers "what fits my budget?" The homepage sections (Top Rated, Newest) serve as a curated entry point that makes the platform feel alive.

**Without this:** Restaurants appear in arbitrary database order (usually by ID — the order they were created). There's no way for a user to find the best-rated restaurants without scrolling through everything. The homepage has no curated content. You lose one mandatory feature checkbox.

**Example:** User clicks "Top Rated" sort button → URL becomes `/restaurants/?sort=rating` → the view annotates each restaurant with its `Avg('reviews__rating')` and orders descending → the 4.8★ restaurant appears first, the 2.5★ appears last. On the homepage, "Top Rated" shows the 5 highest-rated restaurants, and "Just Added" shows the 5 most recently created restaurants.

Update the home view and restaurant list to support sorting:

```python
def restaurant_list(request):
    restaurants = Restaurant.objects.all()

    # ... existing filters ...

    # Sorting
    # sort_by = request.GET.get('sort', '')
    # if sort_by == 'rating':
    #     restaurants = restaurants.annotate(
    #         avg_rating=Avg('reviews__rating')
    #     ).order_by('-avg_rating')
    # elif sort_by == 'newest':
    #     restaurants = restaurants.order_by('-created_at')
    # elif sort_by == 'price_low':
    #     restaurants = restaurants.order_by('price_range')
    # elif sort_by == 'price_high':
    #     restaurants = restaurants.order_by('-price_range')

    pass
```

**Template:** Add sort links/buttons:
```html
<a href="?sort=rating">Top Rated</a>
<a href="?sort=newest">Newest</a>
<a href="?sort=price_low">Price: Low to High</a>
```

### Photo Upload

**What:** You're ensuring the full photo upload pipeline works end-to-end: the form accepts file uploads, the view handles `request.FILES`, photos are saved to the `media/` directory, and templates display them with proper `<img>` tags.

**Why:** Restaurant photos are a mandatory feature and they make THE biggest visual difference. A restaurant listing with a photo of delicious food vs. a gray placeholder — the photo version gets 10x more engagement. Photos also showcase ImageField usage, MEDIA configuration, and file handling, which are all Django skills the professor wants to see.

**Without this:** Every restaurant shows a placeholder icon or broken image. The app looks empty and unfinished. You lose one mandatory feature checkbox. The admin can upload photos, but the frontend forms can't — users who create restaurants through the website have no way to add a photo.

**Example:** Ali creates a new restaurant, clicks "Choose File" on the photo field, selects a JPG of kebabs → the form submits with `enctype="multipart/form-data"` → the view handles `request.FILES` → Django saves the file to `media/restaurants/kebab_aKd3x.jpg` (auto-renamed to avoid conflicts) → the detail page shows the photo in the hero banner → the card on the list page shows it as a thumbnail with `object-fit: cover` so it looks good regardless of dimensions.

Already configured in Week 6 (MEDIA_URL/MEDIA_ROOT). Just make sure:

1. `RestaurantForm` includes `'photo'` in fields
2. Form tag has `enctype="multipart/form-data"`
3. View passes `request.FILES` to the form
4. Template displays the photo:

```html
{% if restaurant.photo %}
    <img src="{{ restaurant.photo.url }}" alt="{{ restaurant.name }}">
{% else %}
    <img src="placeholder.jpg" alt="No photo available">
{% endif %}
```

### Checkpoint — What Should Work
- [ ] Menu items can be added/edited/deleted per restaurant
- [ ] Users can favorite/unfavorite restaurants
- [ ] Favorites list page shows all favorited restaurants
- [ ] User profile page shows bio, reviews, favorites
- [ ] Review replies work (one level)
- [ ] Atomic transactions wrap multi-step operations
- [ ] Restaurants can be sorted by rating, newest, price
- [ ] Homepage shows top-rated and newest sections
- [ ] Restaurant photos display correctly

---

## WEEKS 12-13 — Bonus Features + Polish

### Suggested Team Split
- **Person A (you):** JavaScript elements (star rating widget, dynamic filter) — leverage your JS/Svelte experience
- **Person B:** CSS & Responsive design with Bootstrap
- **Person C:** Advanced filtering (combined multi-filter)
- **Person D:** Review likes OR Map integration

### CSS & Responsive (Bonus)

With Bootstrap already added in Week 7, enhance:
- Restaurant cards in a responsive grid (`row` + `col-md-4`)
- Proper navbar with hamburger menu on mobile
- Card components for restaurants, reviews
- Badges for price range, category
- Consistent spacing and typography

### JavaScript Element (Bonus)

**Interactive Star Rating Widget:**

Instead of a boring number dropdown, create clickable stars.

```html
<!-- In the review form template -->
<div id="star-rating">
    <span class="star" data-value="1">&#9733;</span>
    <span class="star" data-value="2">&#9733;</span>
    <span class="star" data-value="3">&#9733;</span>
    <span class="star" data-value="4">&#9733;</span>
    <span class="star" data-value="5">&#9733;</span>
</div>
<input type="hidden" name="rating" id="rating-input" value="0">
```

```javascript
// Logic:
// 1. Listen for click on each .star element
// 2. On click, get the data-value attribute
// 3. Set the hidden input value to that number
// 4. Highlight all stars up to and including the clicked one
// 5. On hover, preview the rating (highlight on mouseover, reset on mouseout)
//
// document.querySelectorAll('.star').forEach(star => {
//     star.addEventListener('click', function() {
//         const value = this.dataset.value;
//         document.getElementById('rating-input').value = value;
//         highlightStars(value);
//     });
// });
//
// function highlightStars(count) {
//     document.querySelectorAll('.star').forEach(star => {
//         star.style.color = star.dataset.value <= count ? '#ffc107' : '#ccc';
//     });
// }
```

**Other JS ideas you could do with your Svelte background:**
- Dynamic filter that updates results without page reload (fetch API)
- Modal popups for delete confirmations
- Auto-complete in the search bar
- Image preview before upload

### Advanced Filtering (Bonus)

Combine all filters simultaneously. The logic in `restaurant_list` already supports this if you chain `.filter()` calls — each one narrows the queryset further:

```python
# These chain naturally:
restaurants = Restaurant.objects.all()
if category: restaurants = restaurants.filter(category_id=category)
if location: restaurants = restaurants.filter(location_id=location)
if price:    restaurants = restaurants.filter(price_range=price)
if min_rating:
    restaurants = restaurants.annotate(
        avg_rating=Avg('reviews__rating')
    ).filter(avg_rating__gte=min_rating)
```

### Review Likes (Bonus)

Create a `ReviewLike` model:
```python
# Fields: review (FK), user (FK), is_like (BooleanField — True=like, False=dislike)
# unique_together = ['review', 'user']
```

Toggle view (same pattern as favorites toggle). Display count in template. Sort reviews by net likes (likes minus dislikes).

### Map Integration (Bonus)

Add latitude/longitude fields to Restaurant model, then embed a Google Maps iframe:
```html
<iframe
    src="https://maps.google.com/maps?q={{ restaurant.latitude }},{{ restaurant.longitude }}&output=embed"
    width="100%" height="300" style="border:0;" loading="lazy">
</iframe>
```

---

## WEEK 14-15 — Final Demo + Report

### Demo Script (10 minutes)

| Time | What | Who |
|---|---|---|
| 0-1 min | Intro: "This is QueryCuisine, a restaurant review platform" | Person A |
| 1-3 min | Live: register new user, log in | Person A |
| 3-5 min | Live: browse restaurants, use search + filters, view detail page | Person B |
| 5-7 min | Live: write a review, reply to a review, manage favorites | Person C |
| 7-8 min | Live: create restaurant, add menu items, upload photo | Person D |
| 8-9 min | Technical: model design, atomic transactions, bonus features | Whoever built them |
| 9-10 min | Q&A | Everyone |

### Report Template (6-8 Pages, Hardcopy)

**Page 1: Title Page**
- QueryCuisine — Restaurant Review & Discovery Platform
- Group member names and student IDs
- CSE 220 Web Programming, Spring 2026
- Date

**Page 2: Project Description**
- What QueryCuisine does (2-3 paragraphs)
- User stories: "As a user, I can..." (list 5-6 key user stories)

**Page 3: System Architecture**
- Django MVT diagram applied to QueryCuisine
- How URLs route to views, views query models, models populate templates
- Brief description of each app component

**Page 4: Database Design**
- ER diagram showing all models and relationships
- Brief explanation of key design decisions (why OneToOne for profile, why unique_together for reviews, etc.)

**Page 5-6: Screenshots**
- Home page, restaurant list, restaurant detail, review form, admin panel, user profile, favorites
- Caption each screenshot briefly

**Page 7: Feature Checklist**

| Feature | Status | Notes |
|---|---|---|
| Restaurant CRUD | Done | |
| Category System | Done | |
| ... | ... | ... |

**Page 8: Challenges, Solutions, Individual Contributions**
- 2-3 challenges you faced and how you solved them
- Table of who built what (backed by GitHub commits)
- GitHub repository link

---

# PART 4: Database Design — Full ER Diagram

```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│   Category   │     │   Location   │     │     User     │
├──────────────┤     ├──────────────┤     │  (built-in)  │
│ id (PK)      │     │ id (PK)      │     ├──────────────┤
│ name         │     │ city         │     │ id (PK)      │
│ slug         │     │ district     │     │ username     │
└──────┬───────┘     └──────┬───────┘     │ email        │
       │                    │             │ password     │
       │  FK                │  FK         └──┬───┬───┬──┘
       │                    │                │   │   │
       ▼                    ▼                │   │   │
┌─────────────────────────────────────┐      │   │   │
│            Restaurant               │◄─────┘   │   │
├─────────────────────────────────────┤  FK       │   │
│ id (PK)                             │(created_by)   │
│ name                                │           │   │
│ description                         │           │   │
│ address                             │           │   │
│ phone                               │           │   │
│ price_range (€/€€/€€€)             │           │   │
│ photo (ImageField)                  │           │   │
│ category_id (FK → Category)         │           │   │
│ location_id (FK → Location)         │           │   │
│ created_by_id (FK → User)           │           │   │
│ created_at                          │           │   │
│ updated_at                          │           │   │
└──┬──────┬──────┬──────┬─────────────┘           │   │
   │      │      │      │                         │   │
   │      │      │      │    ┌────────────────┐   │   │
   │      │      │      └───►│ OpeningHours   │   │   │
   │      │      │           ├────────────────┤   │   │
   │      │      │           │ id (PK)        │   │   │
   │      │      │           │ restaurant(FK) │   │   │
   │      │      │           │ day_of_week    │   │   │
   │      │      │           │ open_time      │   │   │
   │      │      │           │ close_time     │   │   │
   │      │      │           └────────────────┘   │   │
   │      │      │                                │   │
   │      │      │    ┌────────────────┐          │   │
   │      │      └───►│   MenuItem     │          │   │
   │      │           ├────────────────┤          │   │
   │      │           │ id (PK)        │          │   │
   │      │           │ restaurant(FK) │          │   │
   │      │           │ name           │          │   │
   │      │           │ description    │          │   │
   │      │           │ price          │          │   │
   │      │           │ category       │          │   │
   │      │           └────────────────┘          │   │
   │      │                                       │   │
   │      │    ┌─────────────────────┐            │   │
   │      └───►│     Favorite        │◄───────────┘   │
   │           ├─────────────────────┤                 │
   │           │ id (PK)             │                 │
   │           │ user_id (FK → User) │                 │
   │           │ restaurant_id (FK)  │                 │
   │           │ added_at            │                 │
   │           │ UNIQUE(user, rest.) │                 │
   │           └─────────────────────┘                 │
   │                                                   │
   │    ┌─────────────────────┐                        │
   └───►│      Review         │◄───────────────────────┘
        ├─────────────────────┤
        │ id (PK)             │         ┌──────────────────┐
        │ restaurant_id (FK)  │         │   ReviewReply    │
        │ user_id (FK → User) │         ├──────────────────┤
        │ rating (1-5)        │────────►│ id (PK)          │
        │ comment             │  FK     │ review_id (FK)   │
        │ created_at          │         │ user_id (FK)     │
        │ UNIQUE(user, rest.) │         │ text             │
        └─────────────────────┘         │ created_at       │
                                        └──────────────────┘

┌─────────────────────┐
│    UserProfile      │
├─────────────────────┤
│ id (PK)             │
│ user (1:1 → User)   │
│ bio                 │
└─────────────────────┘
```

**Relationship Summary:**
| From | To | Type | Meaning |
|---|---|---|---|
| Restaurant → Category | Many-to-One | Many restaurants can be "Turkish" |
| Restaurant → Location | Many-to-One | Many restaurants in "Kadıköy" |
| Restaurant → User | Many-to-One | A user can create many restaurants |
| Review → Restaurant | Many-to-One | A restaurant has many reviews |
| Review → User | Many-to-One | A user writes many reviews |
| ReviewReply → Review | Many-to-One | A review has many replies |
| Favorite → User + Restaurant | Many-to-Many (through) | Users favorite many restaurants |
| UserProfile → User | One-to-One | Each user has one profile |
| MenuItem → Restaurant | Many-to-One | A restaurant has many menu items |
| OpeningHours → Restaurant | Many-to-One | A restaurant has 7 hour entries |

---

# PART 5: Common Gotchas & Tips

### Django-Specific Pitfalls

1. **Forgot to run migrations** — If you change `models.py` and see "no such column" errors, you forgot `makemigrations` + `migrate`.

2. **Circular imports** — If `forms.py` imports from `models.py` and `views.py` imports from both, that's fine. But never import views from models.

3. **Template not found** — Check that `DIRS` in settings is correct and that your template path matches exactly (case-sensitive).

4. **CSRF token missing** — Every POST form needs `{% csrf_token %}`. Without it, Django rejects the form with a 403 error.

5. **Static files not loading** — Run `python manage.py collectstatic` in production. In development with `DEBUG=True`, they should work automatically.

6. **ImageField requires Pillow** — Already installed in setup, but if a teammate gets an error, they need to `pip install pillow`.

7. **`related_name` conflicts** — If two ForeignKeys point to the same model, you must set different `related_name` values on each.

### Git Pitfalls

1. **"I pulled and got merge conflicts"** — Open the conflicting file. Look for `<<<<<<< HEAD`, `=======`, `>>>>>>> branch`. Keep the right code, delete the markers, commit.

2. **"I accidentally committed db.sqlite3"** — Run `git rm --cached db.sqlite3`, commit, then make sure `.gitignore` has it listed.

3. **"My teammate's code broke mine"** — This is normal. Read the error, check `git log` to see what changed, fix it together.

### Performance Tips

1. Use `select_related('category', 'location')` when querying restaurants to avoid N+1 queries (one query instead of one per restaurant for related data).

2. Use `prefetch_related('reviews')` when you need to access reviews for a list of restaurants.

3. Use `annotate()` with `Avg` for average ratings instead of computing in Python — let the database do the math.

---

# Quick Reference Card

```
DAILY WORKFLOW:
  source venv/bin/activate
  git pull
  python manage.py runserver
  ... work ...
  git add <files>
  git commit -m "descriptive message"
  git push

AFTER CHANGING MODELS:
  python manage.py makemigrations
  python manage.py migrate

CREATE ADMIN USER:
  python manage.py createsuperuser

INSTALL NEW PACKAGE:
  pip install <package>
  pip freeze > requirements.txt
  git add requirements.txt
  git commit -m "added <package> dependency"

TEAMMATE GETS NEW PACKAGES:
  git pull
  pip install -r requirements.txt

KEY URLS:
  http://127.0.0.1:8000/          → Home
  http://127.0.0.1:8000/admin/    → Admin panel
  http://127.0.0.1:8000/restaurants/ → Restaurant list
```

---

**This plan covers every mandatory feature and all bonus features. Follow it week by week, check off the checkpoints, and you'll have a complete QueryCuisine application by Week 14. Good luck!**

---
---

# PART 6: From Student Project to Sexy Product

This section is what separates "it works" from "holy shit, a student made this?" Your professor and classmates will notice the difference immediately.

---

## 6.1 Design System — The QueryCuisine Brand

### Color Palette

Don't use random colors. Pick a palette and stick to it everywhere.

```css
:root {
    /* Primary — Warm orange/red (food = warmth, appetite) */
    --primary: #E63946;
    --primary-hover: #C1121F;
    --primary-light: #FFF0F0;

    /* Secondary — Deep navy (trust, professionalism) */
    --secondary: #1D3557;
    --secondary-light: #457B9D;

    /* Accents */
    --accent: #F4A261;        /* Warm gold — for stars, highlights */
    --accent-green: #2A9D8F;  /* Teal — for success states, "open now" */

    /* Neutrals */
    --bg: #FAFAFA;            /* Page background — NOT pure white */
    --bg-card: #FFFFFF;       /* Card background */
    --text-primary: #1A1A2E;  /* Main text — NOT pure black */
    --text-secondary: #6C757D;/* Muted text */
    --text-light: #ADB5BD;    /* Placeholders, timestamps */
    --border: #E9ECEF;        /* Subtle borders */
    --border-hover: #DEE2E6;

    /* Shadows — layered for depth */
    --shadow-sm: 0 1px 2px rgba(0,0,0,0.04);
    --shadow-md: 0 4px 12px rgba(0,0,0,0.08);
    --shadow-lg: 0 8px 30px rgba(0,0,0,0.12);
    --shadow-hover: 0 8px 25px rgba(0,0,0,0.15);

    /* Border Radius */
    --radius-sm: 6px;
    --radius-md: 12px;
    --radius-lg: 20px;
    --radius-full: 9999px;    /* For pills, avatars */

    /* Transitions */
    --transition-fast: 150ms ease;
    --transition-normal: 250ms ease;
    --transition-slow: 400ms cubic-bezier(0.16, 1, 0.3, 1);
}
```

### Typography

```css
/* Import a clean font pair — one for headings, one for body */
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Inter:wght@400;500;600&display=swap');

body {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    font-size: 15px;
    line-height: 1.6;
    color: var(--text-primary);
    background: var(--bg);
    -webkit-font-smoothing: antialiased;
}

h1, h2, h3, h4, h5 {
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-weight: 700;
    line-height: 1.2;
    letter-spacing: -0.02em;  /* Tighter letter spacing = modern look */
}

h1 { font-size: 2.5rem; }
h2 { font-size: 1.85rem; }
h3 { font-size: 1.4rem; }
```

**Why this matters:** Default browser fonts scream "student project." Two well-chosen Google Fonts instantly elevate the entire feel. `Plus Jakarta Sans` is modern and distinctive. `Inter` is the gold standard for UI body text.

### The CSS/JS File Structure

```
static/
├── css/
│   └── style.css          ← All your custom CSS
├── js/
│   └── main.js            ← All your custom JavaScript
└── images/
    ├── logo.svg           ← QueryCuisine logo
    ├── hero-bg.jpg        ← Homepage hero background
    ├── placeholder.jpg    ← Default restaurant photo
    └── empty-state.svg    ← Illustration for empty results
```

Configure static files in `settings.py`:
```python
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
```

Use in templates:
```html
{% load static %}
<link rel="stylesheet" href="{% static 'css/style.css' %}">
```

---

## 6.2 The Base Template — Done Right

This is what `base.html` should actually look like for a professional product:

```html
{% load static %}
<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}QueryCuisine{% endblock %} | Discover & Review Restaurants</title>

    <!-- Favicon -->
    <link rel="icon" type="image/svg+xml" href="{% static 'images/logo.svg' %}">

    <!-- Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">

    <!-- Bootstrap 5 -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">

    <!-- Bootstrap Icons (much better than plain text) -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.0/font/bootstrap-icons.css" rel="stylesheet">

    <!-- Your Custom CSS (loads AFTER Bootstrap so it can override) -->
    <link rel="stylesheet" href="{% static 'css/style.css' %}">

    {% block extra_css %}{% endblock %}
</head>
<body>
    <!-- ===== NAVBAR ===== -->
    <nav class="navbar navbar-expand-lg sticky-top">
        <div class="container">
            <!-- Logo -->
            <a class="navbar-brand" href="{% url 'home' %}">
                <span class="brand-icon">
                    <i class="bi bi-pin-map-fill"></i>
                </span>
                <span class="brand-text">QueryCuisine</span>
            </a>

            <!-- Mobile hamburger -->
            <button class="navbar-toggler" type="button"
                    data-bs-toggle="collapse" data-bs-target="#navbarMain">
                <i class="bi bi-list"></i>
            </button>

            <!-- Nav links -->
            <div class="collapse navbar-collapse" id="navbarMain">
                <!-- Search bar in navbar -->
                <form class="nav-search mx-auto" method="get"
                      action="{% url 'restaurant_list' %}">
                    <i class="bi bi-search"></i>
                    <input type="text" name="q"
                           placeholder="Search restaurants, cuisines, locations..."
                           value="{{ request.GET.q }}">
                </form>

                <ul class="navbar-nav ms-auto">
                    <li class="nav-item">
                        <a class="nav-link" href="{% url 'restaurant_list' %}">
                            <i class="bi bi-compass"></i> Explore
                        </a>
                    </li>

                    {% if user.is_authenticated %}
                        <li class="nav-item">
                            <a class="nav-link" href="{% url 'restaurant_create' %}">
                                <i class="bi bi-plus-circle"></i> Add Restaurant
                            </a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="{% url 'favorites_list' %}">
                                <i class="bi bi-heart"></i> Favorites
                            </a>
                        </li>
                        <li class="nav-item dropdown">
                            <a class="nav-link dropdown-toggle" href="#"
                               data-bs-toggle="dropdown">
                                <div class="user-avatar">
                                    {{ user.username|first|upper }}
                                </div>
                            </a>
                            <ul class="dropdown-menu dropdown-menu-end">
                                <li class="dropdown-header">
                                    Signed in as <strong>{{ user.username }}</strong>
                                </li>
                                <li><hr class="dropdown-divider"></li>
                                <li>
                                    <a class="dropdown-item" href="{% url 'profile' %}">
                                        <i class="bi bi-person"></i> My Profile
                                    </a>
                                </li>
                                <li>
                                    <a class="dropdown-item"
                                       href="{% url 'favorites_list' %}">
                                        <i class="bi bi-heart"></i> My Favorites
                                    </a>
                                </li>
                                <li><hr class="dropdown-divider"></li>
                                <li>
                                    <a class="dropdown-item text-danger"
                                       href="{% url 'logout' %}">
                                        <i class="bi bi-box-arrow-right"></i> Logout
                                    </a>
                                </li>
                            </ul>
                        </li>
                    {% else %}
                        <li class="nav-item">
                            <a class="nav-link" href="{% url 'login' %}">Log In</a>
                        </li>
                        <li class="nav-item">
                            <a class="btn btn-primary btn-sm ms-2"
                               href="{% url 'register' %}">
                                Sign Up
                            </a>
                        </li>
                    {% endif %}
                </ul>
            </div>
        </div>
    </nav>

    <!-- ===== MESSAGES (success/error notifications) ===== -->
    {% if messages %}
    <div class="container mt-3">
        {% for message in messages %}
            <div class="alert alert-{{ message.tags }} alert-dismissible fade show">
                {% if message.tags == 'success' %}
                    <i class="bi bi-check-circle-fill me-2"></i>
                {% elif message.tags == 'error' %}
                    <i class="bi bi-exclamation-triangle-fill me-2"></i>
                {% endif %}
                {{ message }}
                <button type="button" class="btn-close"
                        data-bs-dismiss="alert"></button>
            </div>
        {% endfor %}
    </div>
    {% endif %}

    <!-- ===== MAIN CONTENT ===== -->
    <main>
        {% block content %}{% endblock %}
    </main>

    <!-- ===== FOOTER ===== -->
    <footer class="site-footer">
        <div class="container">
            <div class="row">
                <div class="col-md-4">
                    <h5><i class="bi bi-pin-map-fill"></i> QueryCuisine</h5>
                    <p class="text-muted">
                        Discover the best restaurants, read reviews from real diners,
                        and share your own dining experiences.
                    </p>
                </div>
                <div class="col-md-2">
                    <h6>Explore</h6>
                    <ul class="footer-links">
                        <li><a href="{% url 'restaurant_list' %}">All Restaurants</a></li>
                        <li><a href="{% url 'restaurant_list' %}?sort=rating">Top Rated</a></li>
                        <li><a href="{% url 'restaurant_list' %}?sort=newest">New Places</a></li>
                    </ul>
                </div>
                <div class="col-md-2">
                    <h6>Company</h6>
                    <ul class="footer-links">
                        <li><a href="{% url 'about' %}">About Us</a></li>
                        <li><a href="{% url 'contact' %}">Contact</a></li>
                    </ul>
                </div>
                <div class="col-md-4">
                    <h6>Stay Connected</h6>
                    <p class="text-muted">
                        Built with Django by students at Acibadem University.
                    </p>
                </div>
            </div>
            <hr>
            <p class="text-center text-muted">
                &copy; 2026 QueryCuisine. All rights reserved.
            </p>
        </div>
    </footer>

    <!-- Bootstrap JS -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    <!-- Your Custom JS -->
    <script src="{% static 'js/main.js' %}"></script>
    {% block extra_js %}{% endblock %}
</body>
</html>
```

### Navbar CSS That Doesn't Look Like Bootstrap Default

```css
/* ===== NAVBAR ===== */
.navbar {
    background: rgba(255, 255, 255, 0.95);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    border-bottom: 1px solid var(--border);
    padding: 0.6rem 0;
    z-index: 1000;
}

.navbar-brand {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-weight: 800;
    font-size: 1.3rem;
    text-decoration: none;
}

.brand-icon {
    background: var(--primary);
    color: white;
    width: 36px;
    height: 36px;
    border-radius: var(--radius-sm);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1rem;
}

.brand-text {
    color: var(--secondary);
}

/* Search bar inside navbar */
.nav-search {
    position: relative;
    max-width: 400px;
    width: 100%;
}

.nav-search i {
    position: absolute;
    left: 14px;
    top: 50%;
    transform: translateY(-50%);
    color: var(--text-light);
    font-size: 0.9rem;
}

.nav-search input {
    width: 100%;
    padding: 0.5rem 1rem 0.5rem 2.5rem;
    border: 1px solid var(--border);
    border-radius: var(--radius-full);
    font-size: 0.85rem;
    background: var(--bg);
    transition: all var(--transition-normal);
}

.nav-search input:focus {
    outline: none;
    border-color: var(--primary);
    box-shadow: 0 0 0 3px var(--primary-light);
    background: white;
}

/* User avatar circle in nav */
.user-avatar {
    width: 32px;
    height: 32px;
    border-radius: 50%;
    background: var(--primary);
    color: white;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 600;
    font-size: 0.85rem;
}
```

---

## 6.3 The Homepage — First Impressions Matter

### Hero Section

The first thing users see. This makes or breaks the impression.

```html
<!-- In home.html -->
{% extends "restaurants/base.html" %}
{% load static %}

{% block content %}
<!-- HERO SECTION -->
<section class="hero">
    <div class="hero-content">
        <h1 class="hero-title">
            Find Your Next<br>
            <span class="hero-highlight">Favorite Spot</span>
        </h1>
        <p class="hero-subtitle">
            Discover {{ total_restaurants }}+ restaurants, read honest reviews,
            and share your dining experiences.
        </p>

        <!-- Hero search bar -->
        <form class="hero-search" method="get"
              action="{% url 'restaurant_list' %}">
            <div class="hero-search-inner">
                <i class="bi bi-search"></i>
                <input type="text" name="q"
                       placeholder="Try 'Turkish', 'Kadikoy', or 'pizza'...">
                <button type="submit">Search</button>
            </div>
        </form>

        <!-- Quick category pills -->
        <div class="hero-categories">
            <span class="hero-categories-label">Popular:</span>
            {% for cat in categories %}
                <a href="{% url 'restaurant_list' %}?category={{ cat.id }}"
                   class="category-pill">
                    {{ cat.name }}
                </a>
            {% endfor %}
        </div>
    </div>
</section>

<!-- TOP RATED SECTION -->
<section class="section">
    <div class="container">
        <div class="section-header">
            <div>
                <h2 class="section-title">Top Rated</h2>
                <p class="section-subtitle">
                    The highest rated spots by our community
                </p>
            </div>
            <a href="{% url 'restaurant_list' %}?sort=rating" class="section-link">
                View all <i class="bi bi-arrow-right"></i>
            </a>
        </div>
        <div class="row g-4">
            {% for restaurant in top_restaurants %}
                <div class="col-md-6 col-lg-3">
                    {% include "restaurants/components/restaurant_card.html" %}
                </div>
            {% empty %}
                <div class="empty-state">
                    <i class="bi bi-emoji-smile"></i>
                    <p>No restaurants yet. Be the first to add one!</p>
                </div>
            {% endfor %}
        </div>
    </div>
</section>

<!-- NEWEST SECTION — same pattern, use newest_restaurants -->
<section class="section">
    <div class="container">
        <div class="section-header">
            <div>
                <h2 class="section-title">Just Added</h2>
                <p class="section-subtitle">Fresh spots waiting to be discovered</p>
            </div>
            <a href="{% url 'restaurant_list' %}?sort=newest" class="section-link">
                View all <i class="bi bi-arrow-right"></i>
            </a>
        </div>
        <div class="row g-4">
            {% for restaurant in newest_restaurants %}
                <div class="col-md-6 col-lg-3">
                    {% include "restaurants/components/restaurant_card.html" %}
                </div>
            {% empty %}
                <p class="text-muted">No restaurants yet.</p>
            {% endfor %}
        </div>
    </div>
</section>
{% endblock %}
```

### Hero CSS

```css
/* ===== HERO ===== */
.hero {
    background: linear-gradient(135deg, var(--secondary) 0%, #0D1B2A 100%);
    color: white;
    padding: 5rem 0 4rem;
    text-align: center;
    position: relative;
    overflow: hidden;
}

/* Subtle animated gradient overlay for visual interest */
.hero::before {
    content: '';
    position: absolute;
    top: -50%;
    left: -50%;
    width: 200%;
    height: 200%;
    background:
        radial-gradient(circle at 30% 50%, rgba(230,57,70,0.15) 0%, transparent 50%),
        radial-gradient(circle at 70% 50%, rgba(244,162,97,0.1) 0%, transparent 50%);
    animation: hero-glow 8s ease-in-out infinite alternate;
}

@keyframes hero-glow {
    from { transform: rotate(0deg); }
    to { transform: rotate(5deg); }
}

.hero-content {
    position: relative;
    z-index: 1;
    max-width: 700px;
    margin: 0 auto;
    padding: 0 1.5rem;
}

.hero-title {
    font-size: 3.2rem;
    font-weight: 800;
    margin-bottom: 1rem;
    letter-spacing: -0.03em;
}

.hero-highlight {
    background: linear-gradient(90deg, var(--primary), var(--accent));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.hero-subtitle {
    font-size: 1.15rem;
    opacity: 0.8;
    margin-bottom: 2rem;
    line-height: 1.7;
}

/* Hero search bar */
.hero-search {
    max-width: 550px;
    margin: 0 auto 1.5rem;
}

.hero-search-inner {
    display: flex;
    align-items: center;
    background: white;
    border-radius: var(--radius-full);
    padding: 0.4rem;
    box-shadow: var(--shadow-lg);
}

.hero-search-inner i {
    color: var(--text-light);
    margin: 0 0.8rem;
    font-size: 1.1rem;
}

.hero-search-inner input {
    flex: 1;
    border: none;
    outline: none;
    font-size: 1rem;
    color: var(--text-primary);
    padding: 0.6rem 0;
}

.hero-search-inner button {
    background: var(--primary);
    color: white;
    border: none;
    border-radius: var(--radius-full);
    padding: 0.7rem 1.8rem;
    font-weight: 600;
    cursor: pointer;
    transition: background var(--transition-fast);
}

.hero-search-inner button:hover {
    background: var(--primary-hover);
}

/* Category pills */
.hero-categories {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 0.5rem;
    flex-wrap: wrap;
}

.hero-categories-label {
    font-size: 0.85rem;
    opacity: 0.6;
}

.category-pill {
    padding: 0.3rem 0.9rem;
    border-radius: var(--radius-full);
    background: rgba(255,255,255,0.15);
    color: white;
    font-size: 0.8rem;
    text-decoration: none;
    transition: background var(--transition-fast);
}

.category-pill:hover {
    background: rgba(255,255,255,0.25);
    color: white;
}

/* Sections */
.section {
    padding: 4rem 0;
}

.section:nth-child(even) {
    background: white;
}

.section-header {
    display: flex;
    justify-content: space-between;
    align-items: flex-end;
    margin-bottom: 2rem;
}

.section-title {
    font-size: 1.85rem;
    margin-bottom: 0.25rem;
}

.section-subtitle {
    color: var(--text-secondary);
    font-size: 0.95rem;
    margin: 0;
}

.section-link {
    color: var(--primary);
    text-decoration: none;
    font-weight: 600;
    font-size: 0.9rem;
    white-space: nowrap;
}

.section-link:hover {
    color: var(--primary-hover);
}
```

---

## 6.4 Restaurant Card Component

Create a reusable card as a **template include** — one file used everywhere.

**File: `templates/restaurants/components/restaurant_card.html`**

```html
<div class="restaurant-card">
    <a href="{% url 'restaurant_detail' restaurant.pk %}" class="restaurant-card-link">
        <!-- Photo -->
        <div class="restaurant-card-image">
            {% if restaurant.photo %}
                <img src="{{ restaurant.photo.url }}"
                     alt="{{ restaurant.name }}" loading="lazy">
            {% else %}
                <div class="restaurant-card-placeholder">
                    <i class="bi bi-camera"></i>
                </div>
            {% endif %}

            <!-- Price badge overlaid on image -->
            <span class="price-badge">{{ restaurant.price_range }}</span>

            <!-- Category tag -->
            <span class="category-tag">{{ restaurant.category.name }}</span>
        </div>

        <!-- Info -->
        <div class="restaurant-card-body">
            <h3 class="restaurant-card-title">{{ restaurant.name }}</h3>

            <div class="restaurant-card-meta">
                <span class="restaurant-rating">
                    <i class="bi bi-star-fill"></i>
                    {{ restaurant.average_rating }}
                    <span class="rating-count">({{ restaurant.reviews.count }})</span>
                </span>
                <span class="restaurant-location">
                    <i class="bi bi-geo-alt"></i>
                    {{ restaurant.location.district }}
                </span>
            </div>

            <p class="restaurant-card-desc">
                {{ restaurant.description|truncatewords:15 }}
            </p>
        </div>
    </a>
</div>
```

**Note:** `truncatewords:15` is a Django template filter — cuts text to 15 words and adds "...". Perfect for card previews.

```css
/* ===== RESTAURANT CARD ===== */
.restaurant-card {
    background: var(--bg-card);
    border-radius: var(--radius-md);
    overflow: hidden;
    border: 1px solid var(--border);
    transition: all var(--transition-normal);
    height: 100%;
}

.restaurant-card:hover {
    transform: translateY(-4px);
    box-shadow: var(--shadow-hover);
    border-color: transparent;
}

.restaurant-card-link {
    text-decoration: none;
    color: inherit;
    display: flex;
    flex-direction: column;
    height: 100%;
}

.restaurant-card-image {
    position: relative;
    height: 200px;
    overflow: hidden;
    background: var(--bg);
}

.restaurant-card-image img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform var(--transition-slow);
}

.restaurant-card:hover .restaurant-card-image img {
    transform: scale(1.05);
}

.restaurant-card-placeholder {
    width: 100%;
    height: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    background: linear-gradient(135deg, #f5f7fa, #c3cfe2);
    color: var(--text-light);
    font-size: 2rem;
}

.price-badge {
    position: absolute;
    top: 12px;
    right: 12px;
    background: rgba(0,0,0,0.7);
    color: white;
    padding: 0.2rem 0.6rem;
    border-radius: var(--radius-sm);
    font-size: 0.8rem;
    font-weight: 600;
    backdrop-filter: blur(4px);
}

.category-tag {
    position: absolute;
    bottom: 12px;
    left: 12px;
    background: white;
    color: var(--text-primary);
    padding: 0.2rem 0.7rem;
    border-radius: var(--radius-full);
    font-size: 0.75rem;
    font-weight: 600;
    box-shadow: var(--shadow-sm);
}

.restaurant-card-body {
    padding: 1rem 1.2rem 1.2rem;
    flex: 1;
    display: flex;
    flex-direction: column;
}

.restaurant-card-title {
    font-size: 1.05rem;
    font-weight: 700;
    margin-bottom: 0.4rem;
}

.restaurant-card-meta {
    display: flex;
    align-items: center;
    gap: 1rem;
    font-size: 0.85rem;
    color: var(--text-secondary);
    margin-bottom: 0.5rem;
}

.restaurant-rating {
    color: var(--accent);
    font-weight: 600;
}

.restaurant-rating .rating-count {
    color: var(--text-light);
    font-weight: 400;
}

.restaurant-card-desc {
    font-size: 0.85rem;
    color: var(--text-secondary);
    margin: 0;
    line-height: 1.5;
}
```

---

## 6.5 Restaurant Detail Page — The Showpiece

This is the most complex and visually impressive page.

### Layout Structure

```html
{% extends "restaurants/base.html" %}
{% load static %}

{% block content %}
<div class="restaurant-detail">
    <!-- HERO BANNER with restaurant photo -->
    <div class="detail-hero">
        {% if restaurant.photo %}
            <img src="{{ restaurant.photo.url }}" alt="{{ restaurant.name }}">
        {% endif %}
        <div class="detail-hero-overlay">
            <div class="container">
                <div class="detail-hero-content">
                    <span class="detail-category">{{ restaurant.category.name }}</span>
                    <h1>{{ restaurant.name }}</h1>
                    <div class="detail-meta">
                        <span class="detail-rating">
                            {% with avg=restaurant.average_rating %}
                                {% for i in "12345" %}
                                    {% if forloop.counter <= avg %}
                                        <i class="bi bi-star-fill"></i>
                                    {% else %}
                                        <i class="bi bi-star"></i>
                                    {% endif %}
                                {% endfor %}
                            {% endwith %}
                            <strong>{{ restaurant.average_rating }}</strong>
                            ({{ reviews.count }} reviews)
                        </span>
                        <span>
                            <i class="bi bi-geo-alt-fill"></i> {{ restaurant.location }}
                        </span>
                        <span>
                            <i class="bi bi-cash"></i> {{ restaurant.price_range }}
                        </span>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <div class="container">
        <div class="row g-4 mt-0">
            <!-- LEFT COLUMN — Main content -->
            <div class="col-lg-8">

                <!-- ABOUT -->
                <div class="detail-section">
                    <h2><i class="bi bi-info-circle"></i> About</h2>
                    <p>{{ restaurant.description }}</p>
                </div>

                <!-- MENU -->
                <div class="detail-section">
                    <h2><i class="bi bi-book"></i> Menu</h2>
                    {% for item in menu_items %}
                        <div class="menu-item">
                            <div class="menu-item-info">
                                <h4>{{ item.name }}</h4>
                                <p>{{ item.description }}</p>
                                <span class="menu-category-badge">{{ item.category }}</span>
                            </div>
                            <span class="menu-item-price">{{ item.price }} TL</span>
                        </div>
                    {% empty %}
                        <p class="text-muted">No menu items added yet.</p>
                    {% endfor %}
                </div>

                <!-- REVIEWS -->
                <div class="detail-section">
                    <h2>
                        <i class="bi bi-chat-square-text"></i>
                        Reviews ({{ reviews.count }})
                    </h2>

                    <!-- Review form (if logged in and hasn't reviewed) -->
                    {% if user.is_authenticated and not user_review %}
                        <div class="review-form-card">
                            <h4>Write a Review</h4>
                            <form method="post" id="review-form">
                                {% csrf_token %}
                                <div id="star-rating" class="star-rating-widget">
                                    <span class="star" data-value="1">&#9733;</span>
                                    <span class="star" data-value="2">&#9733;</span>
                                    <span class="star" data-value="3">&#9733;</span>
                                    <span class="star" data-value="4">&#9733;</span>
                                    <span class="star" data-value="5">&#9733;</span>
                                    <span class="rating-text" id="rating-text">
                                        Select a rating
                                    </span>
                                </div>
                                <input type="hidden" name="rating"
                                       id="rating-input" value="0" required>
                                <textarea name="comment" class="form-control"
                                    rows="3"
                                    placeholder="Share your experience..."></textarea>
                                <button type="submit" class="btn btn-primary mt-2">
                                    <i class="bi bi-send"></i> Submit Review
                                </button>
                            </form>
                        </div>
                    {% elif user_review %}
                        <div class="alert alert-info">
                            <i class="bi bi-check-circle"></i>
                            You've already reviewed this restaurant.
                        </div>
                    {% else %}
                        <p>
                            <a href="{% url 'login' %}">Log in</a> to write a review.
                        </p>
                    {% endif %}

                    <!-- Review list -->
                    {% for review in reviews %}
                        <div class="review-card">
                            <div class="review-header">
                                <div class="review-user-avatar">
                                    {{ review.user.username|first|upper }}
                                </div>
                                <div>
                                    <strong>{{ review.user.username }}</strong>
                                    <div class="review-stars">
                                        {% for i in "12345" %}
                                            {% if forloop.counter <= review.rating %}
                                                <i class="bi bi-star-fill"></i>
                                            {% else %}
                                                <i class="bi bi-star"></i>
                                            {% endif %}
                                        {% endfor %}
                                    </div>
                                </div>
                                <span class="review-date">
                                    {{ review.created_at|timesince }} ago
                                </span>
                            </div>
                            <p class="review-comment">{{ review.comment }}</p>

                            <!-- Replies -->
                            {% for reply in review.replies.all %}
                                <div class="review-reply">
                                    <strong>{{ reply.user.username }}</strong>
                                    <p>{{ reply.text }}</p>
                                    <small class="text-muted">
                                        {{ reply.created_at|timesince }} ago
                                    </small>
                                </div>
                            {% endfor %}

                            <!-- Reply form -->
                            {% if user.is_authenticated %}
                                <form method="post"
                                      action="{% url 'reply_to_review' review.pk %}"
                                      class="reply-form">
                                    {% csrf_token %}
                                    <input type="text" name="text" class="form-control"
                                           placeholder="Write a reply...">
                                    <button type="submit" class="btn btn-sm btn-outline-secondary">
                                        Reply
                                    </button>
                                </form>
                            {% endif %}
                        </div>
                    {% empty %}
                        <div class="empty-state">
                            <i class="bi bi-chat-square"></i>
                            <p>No reviews yet. Be the first to share your experience!</p>
                        </div>
                    {% endfor %}
                </div>
            </div>

            <!-- RIGHT COLUMN — Sidebar -->
            <div class="col-lg-4">
                <div class="info-sidebar">
                    <!-- Favorite button -->
                    {% if user.is_authenticated %}
                        <form method="post"
                              action="{% url 'toggle_favorite' restaurant.pk %}">
                            {% csrf_token %}
                            <button type="submit"
                                class="btn {% if is_favorited %}btn-danger{% else %}btn-outline-danger{% endif %} w-100 mb-3 btn-favorite"
                                data-url="{% url 'toggle_favorite' restaurant.pk %}">
                                <i class="bi {% if is_favorited %}bi-heart-fill{% else %}bi-heart{% endif %}"></i>
                                {% if is_favorited %}Saved to Favorites{% else %}Add to Favorites{% endif %}
                            </button>
                        </form>
                    {% endif %}

                    <!-- Contact Info -->
                    <div class="sidebar-section">
                        <h5>Contact</h5>
                        <div class="sidebar-item">
                            <i class="bi bi-geo-alt"></i>
                            <span>{{ restaurant.address }}</span>
                        </div>
                        <div class="sidebar-item">
                            <i class="bi bi-telephone"></i>
                            <span>{{ restaurant.phone }}</span>
                        </div>
                    </div>

                    <!-- Opening Hours -->
                    <div class="sidebar-section">
                        <h5>Opening Hours</h5>
                        {% for hours in opening_hours %}
                            <div class="hours-row">
                                <span>{{ hours.get_day_of_week_display }}</span>
                                <span>{{ hours.open_time|time:"H:i" }} - {{ hours.close_time|time:"H:i" }}</span>
                            </div>
                        {% empty %}
                            <p class="text-muted">Hours not available</p>
                        {% endfor %}
                    </div>

                    <!-- Edit/Delete (if owner) -->
                    {% if user == restaurant.created_by %}
                        <div class="sidebar-section">
                            <h5>Manage</h5>
                            <a href="{% url 'restaurant_edit' restaurant.pk %}"
                               class="btn btn-outline-secondary w-100 mb-2">
                                <i class="bi bi-pencil"></i> Edit Restaurant
                            </a>
                            <a href="{% url 'restaurant_delete' restaurant.pk %}"
                               class="btn btn-outline-danger w-100">
                                <i class="bi bi-trash"></i> Delete
                            </a>
                        </div>
                    {% endif %}
                </div>
            </div>
        </div>
    </div>
</div>
{% endblock %}
```

### Detail Page CSS

```css
/* ===== DETAIL HERO ===== */
.detail-hero {
    position: relative;
    height: 400px;
    overflow: hidden;
    background: var(--secondary);
}

.detail-hero img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}

.detail-hero-overlay {
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
    background: linear-gradient(transparent, rgba(0,0,0,0.8));
    padding: 3rem 0 2rem;
    color: white;
}

.detail-category {
    display: inline-block;
    padding: 0.25rem 0.8rem;
    background: var(--primary);
    border-radius: var(--radius-full);
    font-size: 0.8rem;
    font-weight: 600;
    margin-bottom: 0.5rem;
}

.detail-meta {
    display: flex;
    gap: 1.5rem;
    font-size: 0.95rem;
    opacity: 0.9;
    flex-wrap: wrap;
}

.detail-rating i {
    color: var(--accent);
}

/* ===== SIDEBAR ===== */
.info-sidebar {
    position: sticky;
    top: 80px;
    background: white;
    border-radius: var(--radius-md);
    border: 1px solid var(--border);
    padding: 1.5rem;
}

.sidebar-section {
    padding: 1rem 0;
    border-top: 1px solid var(--border);
}

.sidebar-section h5 {
    font-size: 0.95rem;
    font-weight: 700;
    margin-bottom: 0.75rem;
}

.sidebar-item {
    display: flex;
    gap: 0.75rem;
    align-items: flex-start;
    margin-bottom: 0.5rem;
    font-size: 0.9rem;
    color: var(--text-secondary);
}

.sidebar-item i {
    color: var(--primary);
    margin-top: 3px;
}

.hours-row {
    display: flex;
    justify-content: space-between;
    font-size: 0.85rem;
    padding: 0.3rem 0;
    color: var(--text-secondary);
}

/* ===== DETAIL SECTIONS ===== */
.detail-section {
    background: white;
    border-radius: var(--radius-md);
    border: 1px solid var(--border);
    padding: 1.5rem 2rem;
    margin-bottom: 1.5rem;
}

.detail-section h2 {
    font-size: 1.3rem;
    margin-bottom: 1rem;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}

.detail-section h2 i {
    color: var(--primary);
}

/* ===== MENU ITEMS ===== */
.menu-item {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    padding: 1rem 0;
    border-bottom: 1px solid var(--border);
}

.menu-item:last-child {
    border-bottom: none;
}

.menu-item h4 {
    font-size: 1rem;
    margin-bottom: 0.2rem;
}

.menu-item p {
    font-size: 0.85rem;
    color: var(--text-secondary);
    margin-bottom: 0.3rem;
}

.menu-category-badge {
    font-size: 0.7rem;
    padding: 0.15rem 0.5rem;
    background: var(--bg);
    border-radius: var(--radius-full);
    color: var(--text-secondary);
    font-weight: 600;
}

.menu-item-price {
    font-weight: 700;
    font-size: 1.05rem;
    color: var(--primary);
    white-space: nowrap;
}

/* ===== REVIEWS ===== */
.review-form-card {
    background: var(--bg);
    border-radius: var(--radius-md);
    padding: 1.5rem;
    margin-bottom: 1.5rem;
}

.review-card {
    padding: 1.25rem 0;
    border-bottom: 1px solid var(--border);
}

.review-card:last-child {
    border-bottom: none;
}

.review-header {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    margin-bottom: 0.5rem;
}

.review-user-avatar {
    width: 40px;
    height: 40px;
    border-radius: 50%;
    background: var(--secondary-light);
    color: white;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 700;
    font-size: 0.9rem;
    flex-shrink: 0;
}

.review-stars {
    color: var(--accent);
    font-size: 0.8rem;
}

.review-date {
    margin-left: auto;
    font-size: 0.8rem;
    color: var(--text-light);
}

.review-comment {
    font-size: 0.95rem;
    line-height: 1.6;
    margin: 0;
}

/* Nested replies */
.review-reply {
    margin-left: 3rem;
    margin-top: 0.75rem;
    padding: 0.75rem 1rem;
    background: var(--bg);
    border-radius: var(--radius-sm);
    font-size: 0.9rem;
}

.review-reply p {
    margin: 0.25rem 0;
}

.reply-form {
    display: flex;
    gap: 0.5rem;
    margin-top: 0.75rem;
    margin-left: 3rem;
}

.reply-form input {
    font-size: 0.85rem;
}

/* ===== STAR RATING WIDGET ===== */
.star-rating-widget {
    display: flex;
    align-items: center;
    gap: 0.3rem;
    margin-bottom: 1rem;
}

.star-rating-widget .star {
    font-size: 2rem;
    color: #ddd;
    cursor: pointer;
    transition: color var(--transition-fast), transform var(--transition-fast);
    user-select: none;
}

.star-rating-widget .star:hover {
    transform: scale(1.15);
}

.star-rating-widget .star.active {
    color: var(--accent);
}

.rating-text {
    font-size: 0.85rem;
    color: var(--text-light);
    margin-left: 0.5rem;
}
```

---

## 6.6 Interactive JavaScript Features

**File: `static/js/main.js`**

### Star Rating Widget

```javascript
// ===== STAR RATING WIDGET =====
function initStarRating() {
    const container = document.getElementById('star-rating');
    if (!container) return;

    const input = document.getElementById('rating-input');
    const ratingText = document.getElementById('rating-text');
    const stars = container.querySelectorAll('.star');
    const labels = ['', 'Terrible', 'Poor', 'Average', 'Good', 'Excellent'];

    let currentRating = 0;

    stars.forEach(star => {
        star.addEventListener('click', () => {
            currentRating = parseInt(star.dataset.value);
            input.value = currentRating;
            highlightStars(currentRating);
            if (ratingText) ratingText.textContent = labels[currentRating];
        });

        star.addEventListener('mouseenter', () => {
            highlightStars(parseInt(star.dataset.value));
            if (ratingText) ratingText.textContent = labels[parseInt(star.dataset.value)];
        });

        star.addEventListener('mouseleave', () => {
            highlightStars(currentRating);
            if (ratingText) {
                ratingText.textContent = currentRating ? labels[currentRating] : 'Select a rating';
            }
        });
    });

    function highlightStars(count) {
        stars.forEach(star => {
            star.classList.toggle('active', parseInt(star.dataset.value) <= count);
        });
    }
}
```

### AJAX Favorite Toggle (no page reload)

```javascript
// ===== AJAX FAVORITES =====
function initFavoriteButtons() {
    document.querySelectorAll('.btn-favorite').forEach(btn => {
        btn.addEventListener('click', async function(e) {
            e.preventDefault();
            const form = this.closest('form');
            const url = form.action;
            const csrfToken = form.querySelector('[name=csrfmiddlewaretoken]').value;

            try {
                const response = await fetch(url, {
                    method: 'POST',
                    headers: {
                        'X-CSRFToken': csrfToken,
                        'X-Requested-With': 'XMLHttpRequest',
                    },
                });

                if (response.ok) {
                    const data = await response.json();
                    const icon = this.querySelector('i');

                    if (data.is_favorited) {
                        this.classList.remove('btn-outline-danger');
                        this.classList.add('btn-danger');
                        icon.classList.remove('bi-heart');
                        icon.classList.add('bi-heart-fill');
                        this.innerHTML = '<i class="bi bi-heart-fill"></i> Saved to Favorites';
                        showToast('Added to favorites!');
                    } else {
                        this.classList.remove('btn-danger');
                        this.classList.add('btn-outline-danger');
                        icon.classList.remove('bi-heart-fill');
                        icon.classList.add('bi-heart');
                        this.innerHTML = '<i class="bi bi-heart"></i> Add to Favorites';
                        showToast('Removed from favorites', 'info');
                    }

                    // Little bounce animation
                    this.style.transform = 'scale(1.05)';
                    setTimeout(() => this.style.transform = '', 200);
                }
            } catch (err) {
                showToast('Something went wrong', 'error');
            }
        });
    });
}
```

For this to work, update the Django view to return JSON for AJAX:

```python
# In views.py
from django.http import JsonResponse

@login_required
def toggle_favorite(request, pk):
    restaurant = get_object_or_404(Restaurant, pk=pk)
    favorite = Favorite.objects.filter(user=request.user, restaurant=restaurant)

    if favorite.exists():
        favorite.delete()
        is_favorited = False
    else:
        Favorite.objects.create(user=request.user, restaurant=restaurant)
        is_favorited = True

    # If AJAX request, return JSON instead of redirect
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({'is_favorited': is_favorited})

    return redirect('restaurant_detail', pk=pk)
```

### Toast Notification System

```javascript
// ===== TOAST NOTIFICATIONS =====
function showToast(message, type = 'success') {
    let container = document.getElementById('toast-container');
    if (!container) {
        container = document.createElement('div');
        container.id = 'toast-container';
        container.style.cssText = `
            position: fixed; bottom: 24px; right: 24px; z-index: 9999;
            display: flex; flex-direction: column; gap: 8px;
        `;
        document.body.appendChild(container);
    }

    const icons = {
        success: 'bi-check-circle-fill',
        error: 'bi-exclamation-triangle-fill',
        info: 'bi-info-circle-fill',
    };

    const colors = {
        success: '#2A9D8F',
        error: '#E63946',
        info: '#457B9D',
    };

    const toast = document.createElement('div');
    toast.style.cssText = `
        padding: 0.85rem 1.3rem; border-radius: 12px; color: white;
        background: ${colors[type]}; box-shadow: 0 8px 30px rgba(0,0,0,0.15);
        display: flex; align-items: center; gap: 0.5rem; font-size: 0.9rem;
        font-weight: 500; transform: translateX(120%); transition: transform 300ms ease;
    `;
    toast.innerHTML = `<i class="bi ${icons[type]}"></i> ${message}`;
    container.appendChild(toast);

    // Slide in
    requestAnimationFrame(() => {
        toast.style.transform = 'translateX(0)';
    });

    // Slide out after 3 seconds
    setTimeout(() => {
        toast.style.transform = 'translateX(120%)';
        setTimeout(() => toast.remove(), 300);
    }, 3000);
}
```

### Loading States on Form Submit

```javascript
// ===== LOADING STATES =====
function initFormLoading() {
    document.querySelectorAll('form').forEach(form => {
        form.addEventListener('submit', function() {
            const btn = this.querySelector('button[type="submit"]');
            if (btn && !btn.disabled) {
                btn.disabled = true;
                const originalText = btn.innerHTML;
                btn.innerHTML = `
                    <span class="spinner-border spinner-border-sm me-2"></span>
                    Saving...
                `;
                // Re-enable after 5 seconds as fallback
                setTimeout(() => {
                    btn.disabled = false;
                    btn.innerHTML = originalText;
                }, 5000);
            }
        });
    });
}
```

### Auto-dismiss Django Messages

```javascript
// ===== AUTO-DISMISS ALERTS =====
function initAlertDismiss() {
    document.querySelectorAll('.alert-dismissible').forEach(alert => {
        setTimeout(() => {
            alert.style.transition = 'opacity 500ms ease, transform 500ms ease';
            alert.style.opacity = '0';
            alert.style.transform = 'translateY(-10px)';
            setTimeout(() => alert.remove(), 500);
        }, 4000);
    });
}
```

### Initialize Everything

```javascript
// ===== INIT =====
document.addEventListener('DOMContentLoaded', () => {
    initStarRating();
    initFavoriteButtons();
    initFormLoading();
    initAlertDismiss();
});
```

---

## 6.7 Empty States & Error Pages

### Empty State Component

```css
.empty-state {
    text-align: center;
    padding: 4rem 2rem;
    color: var(--text-secondary);
}

.empty-state-icon {
    width: 80px;
    height: 80px;
    margin: 0 auto 1.5rem;
    border-radius: 50%;
    background: var(--bg);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 2rem;
    color: var(--text-light);
}

.empty-state h3 {
    margin-bottom: 0.5rem;
}

.empty-state p {
    max-width: 400px;
    margin: 0 auto 1.5rem;
}
```

### Custom 404 Page

**File: `templates/404.html`**

```html
{% extends "restaurants/base.html" %}

{% block title %}Page Not Found{% endblock %}

{% block content %}
<div class="error-page">
    <h1 class="error-code">404</h1>
    <h2>Page not found</h2>
    <p>The page you're looking for doesn't exist or has been moved.</p>
    <a href="{% url 'home' %}" class="btn btn-primary">
        <i class="bi bi-house"></i> Back to Home
    </a>
</div>
{% endblock %}
```

```css
.error-page {
    text-align: center;
    padding: 6rem 2rem;
}

.error-code {
    font-size: 8rem;
    font-weight: 800;
    background: linear-gradient(135deg, var(--primary), var(--accent));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    line-height: 1;
    margin-bottom: 1rem;
}
```

**Note:** Custom error pages only show when `DEBUG = False` in settings.py. For the final demo, you may want to set `DEBUG = False` and `ALLOWED_HOSTS = ['*']` temporarily.

---

## 6.8 Django Messages Framework — Polished Feedback

**In `settings.py`** — add Bootstrap-compatible tags:

```python
from django.contrib.messages import constants as messages

MESSAGE_TAGS = {
    messages.DEBUG: 'secondary',
    messages.INFO: 'info',
    messages.SUCCESS: 'success',
    messages.WARNING: 'warning',
    messages.ERROR: 'danger',
}
```

**Use in every view that changes data:**

```python
from django.contrib import messages

# After creating a restaurant:
messages.success(request, f'"{restaurant.name}" has been added!')

# After deleting:
messages.success(request, 'Restaurant deleted successfully.')

# After submitting a review:
messages.success(request, 'Your review has been posted!')

# On permission denied:
messages.warning(request, 'You can only edit your own restaurants.')

# On form errors:
messages.error(request, 'Please fix the errors below.')
```

The base template already displays these with proper icons and auto-dismiss.

---

## 6.9 Professional Form Styling

### Add Bootstrap Classes to Form Widgets

```python
# In forms.py
class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ['name', 'description', 'address', 'phone',
                  'price_range', 'category', 'location', 'photo']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Restaurant name',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Describe the restaurant, its atmosphere, specialties...',
                'rows': 4,
            }),
            'address': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Full address',
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '+90 555 123 4567',
            }),
            'price_range': forms.Select(attrs={'class': 'form-select'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'location': forms.Select(attrs={'class': 'form-select'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
```

### Styled Form Template

```html
<div class="form-page">
    <div class="container">
        <div class="row justify-content-center">
            <div class="col-lg-7">
                <div class="form-card">
                    <h2>Add a Restaurant</h2>
                    <p class="text-muted">
                        Share a great spot with the QueryCuisine community.
                    </p>

                    <form method="post" enctype="multipart/form-data">
                        {% csrf_token %}

                        {% for field in form %}
                            <div class="mb-3">
                                <label class="form-label" for="{{ field.id_for_label }}">
                                    {{ field.label }}
                                    {% if field.field.required %}
                                        <span class="text-danger">*</span>
                                    {% endif %}
                                </label>
                                {{ field }}
                                {% if field.errors %}
                                    <div class="invalid-feedback d-block">
                                        {{ field.errors|first }}
                                    </div>
                                {% endif %}
                                {% if field.help_text %}
                                    <small class="form-text text-muted">
                                        {{ field.help_text }}
                                    </small>
                                {% endif %}
                            </div>
                        {% endfor %}

                        <button type="submit" class="btn btn-primary btn-lg w-100 mt-2">
                            <i class="bi bi-plus-circle me-2"></i>Add Restaurant
                        </button>
                    </form>
                </div>
            </div>
        </div>
    </div>
</div>
```

```css
.form-card {
    background: white;
    border-radius: var(--radius-lg);
    padding: 2.5rem;
    box-shadow: var(--shadow-md);
    margin: 2rem 0;
}

.form-card h2 {
    margin-bottom: 0.25rem;
}

.form-page {
    padding: 2rem 0;
    background: var(--bg);
    min-height: 70vh;
}
```

---

## 6.10 Pagination

Don't dump 100 restaurants on one page. Use Django's Paginator:

```python
# In views.py
from django.core.paginator import Paginator

def restaurant_list(request):
    restaurants = Restaurant.objects.all()
    # ... apply filters ...

    paginator = Paginator(restaurants, 12)  # 12 per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'page_obj': page_obj}
    return render(request, 'restaurants/restaurant_list.html', context)
```

**Template:** Use `page_obj` instead of `restaurants` in your for loop:
```html
{% for restaurant in page_obj %}
    ...
{% endfor %}

{% if page_obj.has_other_pages %}
<nav class="d-flex justify-content-center mt-4">
    <ul class="pagination">
        {% if page_obj.has_previous %}
            <li class="page-item">
                <a class="page-link" href="?page={{ page_obj.previous_page_number }}">
                    <i class="bi bi-chevron-left"></i>
                </a>
            </li>
        {% endif %}

        {% for num in page_obj.paginator.page_range %}
            <li class="page-item {% if page_obj.number == num %}active{% endif %}">
                <a class="page-link" href="?page={{ num }}">{{ num }}</a>
            </li>
        {% endfor %}

        {% if page_obj.has_next %}
            <li class="page-item">
                <a class="page-link" href="?page={{ page_obj.next_page_number }}">
                    <i class="bi bi-chevron-right"></i>
                </a>
            </li>
        {% endif %}
    </ul>
</nav>
{% endif %}
```

**Important:** When combining pagination with filters, you need to preserve filter parameters. The simplest way is to build URLs that include both page and filter params. Add a helper in the view or use a custom template tag.

---

## 6.11 Seed Data Script

Instead of manually clicking through admin, create a management command:

**Create the directory structure:**
```bash
mkdir -p restaurants/management/commands
touch restaurants/management/__init__.py
touch restaurants/management/commands/__init__.py
```

**File: `restaurants/management/commands/seed.py`**

```python
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from restaurants.models import (
    Category, Location, Restaurant, MenuItem, Review, OpeningHours
)
from datetime import time
import random

class Command(BaseCommand):
    help = 'Seeds the database with sample QueryCuisine data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Seeding database...')

        # --- Categories ---
        category_names = [
            'Turkish', 'Italian', 'Fast Food', 'Seafood',
            'Cafe', 'Asian', 'Mexican', 'Fine Dining'
        ]
        categories = {}
        for name in category_names:
            cat, _ = Category.objects.get_or_create(
                name=name,
                defaults={'slug': name.lower().replace(' ', '-')}
            )
            categories[name] = cat

        # --- Locations ---
        location_data = [
            ('Istanbul', 'Kadikoy'),
            ('Istanbul', 'Besiktas'),
            ('Istanbul', 'Uskudar'),
            ('Istanbul', 'Sisli'),
            ('Ankara', 'Cankaya'),
            ('Izmir', 'Alsancak'),
        ]
        locations = {}
        for city, district in location_data:
            loc, _ = Location.objects.get_or_create(city=city, district=district)
            locations[f'{district}'] = loc

        # --- Users ---
        users = []
        user_data = [
            ('demo', 'demo@QueryCuisine.com'),
            ('ali', 'ali@example.com'),
            ('ayse', 'ayse@example.com'),
            ('mehmet', 'mehmet@example.com'),
        ]
        for username, email in user_data:
            user, created = User.objects.get_or_create(
                username=username, defaults={'email': email}
            )
            if created:
                user.set_password('demo1234')
                user.save()
            users.append(user)

        # --- Restaurants ---
        restaurant_data = [
            {
                'name': 'Karadeniz Pide Salonu',
                'description': 'Authentic Black Sea style pide baked in a wood-fired oven. Famous for kusbasili and karisik pide since 1978. The dough is hand-stretched daily and baked at extreme heat for that perfect crispy-yet-chewy texture.',
                'category': 'Turkish',
                'location': 'Kadikoy',
                'price_range': '€',
                'address': 'Caferaga Mah. Moda Cad. No:42, Kadikoy',
                'phone': '+90 216 345 6789',
            },
            {
                'name': 'Trattoria Bella',
                'description': 'Cozy Italian restaurant with handmade pasta, wood-fired pizza, and an extensive wine list. Our chef trained in Naples and brings authentic Southern Italian flavors to Istanbul.',
                'category': 'Italian',
                'location': 'Besiktas',
                'price_range': '€€€',
                'address': 'Akaretler, Suleyman Seba Cad. No:15, Besiktas',
                'phone': '+90 212 987 6543',
            },
            {
                'name': 'Burger Lab',
                'description': 'Gourmet burger joint with creative toppings and hand-cut fries. Our patties are 100% prime beef, never frozen, and our brioche buns are baked fresh every morning.',
                'category': 'Fast Food',
                'location': 'Sisli',
                'price_range': '€€',
                'address': 'Halaskargazi Cad. No:88, Sisli',
                'phone': '+90 212 456 7890',
            },
            {
                'name': 'Deniz Kizi Balik',
                'description': 'Fresh seafood restaurant on the Bosphorus shore. Daily catch from local fishermen, grilled to perfection. The mezes are legendary and the view is unbeatable.',
                'category': 'Seafood',
                'location': 'Uskudar',
                'price_range': '€€€',
                'address': 'Salacak Mah. Sahil Yolu No:7, Uskudar',
                'phone': '+90 216 111 2233',
            },
            {
                'name': 'Kahve Dunyasi Moda',
                'description': 'Specialty coffee shop with single-origin beans roasted in-house. Artisan pastries baked daily. Perfect spot for a quiet morning or productive afternoon.',
                'category': 'Cafe',
                'location': 'Kadikoy',
                'price_range': '€',
                'address': 'Moda Cad. No:22, Kadikoy',
                'phone': '+90 216 333 4455',
            },
            {
                'name': 'Tokyo Ramen House',
                'description': 'Authentic Japanese ramen with rich tonkotsu broth simmered for 18 hours. Also serving gyoza, katsu curry, and matcha desserts.',
                'category': 'Asian',
                'location': 'Besiktas',
                'price_range': '€€',
                'address': 'Sinanpasa Mah. No:34, Besiktas',
                'phone': '+90 212 555 6677',
            },
            {
                'name': 'Sultan Sofra',
                'description': 'Ottoman-inspired fine dining experience in a restored historical mansion. Tasting menus feature modernized classic Ottoman recipes with premium ingredients.',
                'category': 'Fine Dining',
                'location': 'Uskudar',
                'price_range': '€€€',
                'address': 'Fethi Pasa Korusu No:1, Uskudar',
                'phone': '+90 216 777 8899',
            },
            {
                'name': 'Taco Loco',
                'description': 'Vibrant Mexican street food — tacos, burritos, quesadillas, and fresh guacamole made table-side. Margaritas are the best in the city.',
                'category': 'Mexican',
                'location': 'Cankaya',
                'price_range': '€€',
                'address': 'Tunali Hilmi Cad. No:55, Cankaya',
                'phone': '+90 312 444 5566',
            },
        ]

        restaurants = []
        for i, r_data in enumerate(restaurant_data):
            restaurant, created = Restaurant.objects.get_or_create(
                name=r_data['name'],
                defaults={
                    'description': r_data['description'],
                    'category': categories[r_data['category']],
                    'location': locations[r_data['location']],
                    'price_range': r_data['price_range'],
                    'address': r_data['address'],
                    'phone': r_data['phone'],
                    'created_by': users[i % len(users)],
                }
            )
            restaurants.append(restaurant)

            if created:
                # Add opening hours
                for day in range(7):
                    OpeningHours.objects.get_or_create(
                        restaurant=restaurant,
                        day_of_week=day,
                        defaults={
                            'open_time': time(9, 0) if day < 5 else time(10, 0),
                            'close_time': time(22, 0) if day < 5 else time(23, 0),
                        }
                    )

        # --- Menu Items ---
        menu_data = {
            'Karadeniz Pide Salonu': [
                ('Kusbasili Pide', 'Diced lamb with peppers', 160, 'Main'),
                ('Karisik Pide', 'Mixed meat and cheese', 180, 'Main'),
                ('Lahmacun', 'Thin crust Turkish pizza', 80, 'Main'),
                ('Ayran', 'Traditional yogurt drink', 30, 'Drink'),
                ('Kunefe', 'Sweet cheese pastry with syrup', 90, 'Dessert'),
            ],
            'Trattoria Bella': [
                ('Margherita Pizza', 'San Marzano tomatoes, mozzarella, basil', 220, 'Main'),
                ('Carbonara', 'Guanciale, egg yolk, pecorino', 250, 'Main'),
                ('Tiramisu', 'Classic Italian coffee dessert', 140, 'Dessert'),
                ('Chianti Glass', 'House red wine', 120, 'Drink'),
            ],
            'Burger Lab': [
                ('Classic Smash', 'Double patty, cheddar, pickles, special sauce', 200, 'Main'),
                ('Truffle Burger', 'Truffle mayo, gruyere, caramelized onions', 280, 'Main'),
                ('Loaded Fries', 'Cheese sauce, bacon, jalapenos', 120, 'Side'),
                ('Milkshake', 'Vanilla, chocolate, or strawberry', 80, 'Drink'),
            ],
        }

        for restaurant_name, items in menu_data.items():
            try:
                restaurant = Restaurant.objects.get(name=restaurant_name)
                for name, desc, price, cat in items:
                    MenuItem.objects.get_or_create(
                        restaurant=restaurant,
                        name=name,
                        defaults={
                            'description': desc,
                            'price': price,
                            'category': cat,
                        }
                    )
            except Restaurant.DoesNotExist:
                pass

        # --- Reviews ---
        review_comments = [
            (5, 'Absolutely incredible! Best meal I have had in months.'),
            (4, 'Great food and atmosphere. Service was a bit slow but worth the wait.'),
            (5, 'A must-visit! The flavors were authentic and the portions generous.'),
            (3, 'Decent food but nothing special. A bit overpriced for what you get.'),
            (4, 'Really enjoyed the experience. Will definitely come back.'),
            (2, 'Disappointing. The food was cold and the waiter was rude.'),
            (5, 'Perfect date night spot. Romantic ambiance and exquisite food.'),
            (4, 'Solid choice for a casual dinner. Good variety on the menu.'),
        ]

        for restaurant in restaurants:
            reviewers = random.sample(users, min(3, len(users)))
            for j, user in enumerate(reviewers):
                rating, comment = review_comments[(restaurants.index(restaurant) + j) % len(review_comments)]
                Review.objects.get_or_create(
                    restaurant=restaurant,
                    user=user,
                    defaults={
                        'rating': rating,
                        'comment': comment,
                    }
                )

        self.stdout.write(self.style.SUCCESS(
            f'Done! Created {len(restaurants)} restaurants with menus, reviews, and hours.'
        ))
```

**Run it:** `python manage.py seed`

Anyone who clones the repo can seed the database with one command. Your TA will love this.

---

## 6.12 README.md That Impresses

Your README is the first thing anyone sees on GitHub.

```markdown
# QueryCuisine

> A restaurant review & discovery platform built with Django.
> Discover restaurants, read honest reviews, and share your dining experiences.

> **CSE 220 — Web Programming** | Acibadem University | Spring 2026

## Screenshots

(Add 3-4 screenshots of your best-looking pages here)

## Features

- Restaurant discovery with search, category/location/price filters, and sorting
- User authentication (register, login, logout)
- Reviews with 1-5 interactive star ratings and replies
- Personal favorites list
- Restaurant menus and opening hours
- User profiles with review history
- Photo uploads
- Responsive mobile-friendly design

## Tech Stack

- **Backend:** Django 5.x, Python 3.13
- **Database:** SQLite
- **Frontend:** Bootstrap 5, custom CSS, vanilla JavaScript
- **Version Control:** Git + GitHub

## Getting Started

### Prerequisites
- Python 3.10+
- pip

### Installation

    git clone https://github.com/YOUR-USERNAME/QueryCuisine.git
    cd QueryCuisine
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    python manage.py migrate
    python manage.py seed          # Load sample data
    python manage.py createsuperuser
    python manage.py runserver

Visit http://127.0.0.1:8000

## Team

| Name | Role | GitHub |
|------|------|--------|
| ... | ... | ... |
```

---

## 6.13 Final Checklist — "Is This Actually Good?"

### Visual Quality
- [ ] Consistent color palette (no random colors anywhere)
- [ ] Proper font hierarchy (Plus Jakarta Sans headings, Inter body)
- [ ] Cards have subtle shadows and rounded corners
- [ ] Hover effects on all clickable elements (cards lift, buttons shift)
- [ ] Proper spacing (nothing cramped or floating randomly)
- [ ] Images are properly sized with `object-fit: cover` (no stretching)
- [ ] Mobile responsive (test by resizing browser to phone width)
- [ ] Navbar has glassmorphism blur effect
- [ ] Hero section has gradient text and animated background

### UX Quality
- [ ] Every action gives feedback (Django messages + toast notifications)
- [ ] Empty states have friendly messages and icons (not blank pages)
- [ ] Loading spinner on form submissions
- [ ] Navigation makes sense — can always get back to list/home
- [ ] Login/Register are easy to find (nav bar, prominent CTA)
- [ ] Error messages are helpful and styled (not plain text)
- [ ] 404 page is custom with gradient text, not Django's ugly default
- [ ] Star rating widget works with hover preview
- [ ] Favorites toggle without page reload (AJAX)

### Code Quality
- [ ] No hardcoded data anywhere (everything from database)
- [ ] All views use `get_object_or_404` (not raw try/except)
- [ ] Permission checks on all edit/delete views (`created_by == request.user`)
- [ ] CSRF tokens on all POST forms
- [ ] `select_related` / `prefetch_related` on list views
- [ ] `enctype="multipart/form-data"` on forms with file upload
- [ ] Django messages used consistently across all views
- [ ] Atomic transactions on multi-step operations

### Demo Readiness
- [ ] Database has 8+ restaurants across multiple categories/locations
- [ ] Multiple users with reviews (use seed command)
- [ ] All team members can run the project locally
- [ ] All team members can explain any part of the code
- [ ] Demo script rehearsed at least once
- [ ] Seed command works for fresh setup
