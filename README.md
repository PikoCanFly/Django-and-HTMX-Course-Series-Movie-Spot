# Movie Spot - Part 6: User Authentication & Account Management


[Watch the Movie Spot Tutorial on YouTube](https://youtu.be/aCWd4loTl68)  
<br/>
[![Movie Spot - Part-2 Thumbnail](https://img.youtube.com/vi/aCWd4loTl68/hqdefault.jpg)](https://youtu.be/aCWd4loTl68)
Welcome to **Movie Spot Part 6**! In this branch, we focus on building a secure user authentication system and managing user accounts within our Django web app. In this part of the series, you'll learn how to:

- **Set Up User Authentication:**  
  Implement Django's built-in authentication system to handle login, logout, and registration.

- **Create Custom Registration Forms:**  
  Develop a user-friendly registration form (by subclassing Django's UserCreationForm) that works seamlessly with your custom user model.

- **Build a Profile Page:**  
  Create a dedicated profile page where authenticated users can view and manage their account details.

- **Implement Conditional Rendering:**  
  Use Django template logic (e.g., `{% if user.is_authenticated %}`) to display different UI elements based on whether the user is logged in.

- **Secure Your Forms:**  
  Ensure that all forms include CSRF protection for enhanced security.

---


### Cloning the Repository

To get started, clone the repository from GitHub:

```
git clone https://github.com/PikoCanFly/Django-and-HTMX-Course-Series-Movie-Spot.git
cd Django-and-HTMX-Course-Series-Movie-Spot
```

## Accessing the branches:
This repository is organized into branches corresponding to each part of the series. To work with Part-6, run:


```
git checkout part-6
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


**Environment Setup & API Key Reminder**

Make sure you've already set up your environment and obtained your TMDB API key. If you haven't done so yet, you might want to refer back to Part 1 of this series, where we cover creating the .env file and configuring your settings to securely load your API key. This setup is essential for accessing live movie data throughout the entire series.


## Next Steps

To follow along with each stage of the project, simply use git checkout to switch to the corresponding branch (e.g., part-2, part-3, etc.).
