# Movie Spot - Part-1: Basic Project Setup
[Watch on YouTube](https://youtu.be/sm4WL8NGV9A)
<br/>
[![Django + HTMX + Bootstrap Full Stack Project - Beginner Friendly Tutorial Series (Part 1)
](https://img.youtube.com/vi/sm4WL8NGV9A/hqdefault.jpg)](https://youtu.be/sm4WL8NGV9A)


Welcome to **Movie Spot Part-1**! This branch is the starting point of our beginner-friendly, production-ready Django tutorial series. In Part-1, you'll learn how to set up a Django project from scratch with a focus on:

- **Project Structure:**  
  - Creating a new Django project (`movie_spot`)
  - Setting up two Django apps: `movies` for movie-related functionality and `users` for authentication

- **Custom User Model:**  
  - Building a flexible custom user model in the `users` app for secure authentication

- **Base Template with Bootstrap:**  
  - Creating a reusable `base.html` template that uses Bootstrap for responsive design and includes a simple navbar

- **Basic URL Routing & Configuration:**  
  - Setting up URL patterns and basic views to get your project up and running

---

## How to Clone and Access Branches

### Cloning the Repository

To get started, clone the repository from GitHub:

```
git clone https://github.com/PikoCanFly/Django-and-HTMX-Course-Series-Movie-Spot.git
cd Django-and-HTMX-Course-Series-Movie-Spot
```

## Accessing the branches:
This repository is organized into branches corresponding to each part of the series. To work with Part-1, run:


```
git checkout part-1
```
```
Tip: To see all available branches, you can run:
git branch -a
```
If you want to switch to another branch (for example, Part-2 later in the series), simply use:

```
git checkout part-2
```

## Prerequisites
Python 3.10+
Django (installed via pip)
Virtual Environment (recommended)
Git


## Setup Instructions

Once you clone the Repository & Checkout the Correct Branch:

Create and Activate a Virtual Environment:

```
python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate
```
**Install Dependencies:**

Ensure you have a requirements.txt file. Then run:

```
pip install -r requirements.txt
```
Run Migrations:

```
python manage.py makemigrations
python manage.py migrate
```

Access the Application:


## Next Steps

To follow along with each stage of the project, simply use git checkout to switch to the corresponding branch (e.g., part-2, part-3, etc.).



