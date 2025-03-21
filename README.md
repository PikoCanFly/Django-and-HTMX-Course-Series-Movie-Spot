# Movie Spot - Part 5: Building the Movie Detail Page




[Watch the Movie Spot Tutorial on YouTube](https://youtu.be/ldsLB4YDP3c)  
<br/>
[![Movie Spot - Part-2 Thumbnail](https://img.youtube.com/vi/ldsLB4YDP3c/hqdefault.jpg)](https://youtu.be/ldsLB4YDP3c)


Welcome to **Movie Spot Part 5**! In this branch, we focus on creating the movie detail page for our dynamic Django app. This is a key part of our series that turns static pages into interactive, data-driven movie detail views.


## What You'll Learn

- **Dynamic URL Parameters:**  
  Capture the `movie_id` from the URL and pass it to your view.

- **Fetching Movie Data:**  
  Use the TMDB API to retrieve detailed movie information such as title, poster, overview, genres, and cast.

- **Django Functional Views:**  
  Build a view that processes the request, fetches data from an external API, and passes it to the template.

- **Template Rendering:**  
  Utilize Django's templating language—including template tags and filters—to dynamically display movie details.

- **Error Handling:**  
  Implement try/except blocks to gracefully handle API errors and ensure a robust user experience.



### Cloning the Repository

To get started, clone the repository from GitHub:

```
git clone https://github.com/PikoCanFly/Django-and-HTMX-Course-Series-Movie-Spot.git
cd Django-and-HTMX-Course-Series-Movie-Spot
```

## Accessing the branches:
This repository is organized into branches corresponding to each part of the series. To work with Part-2, run:


```
git checkout part-3
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

**Environment Setup & API Key Reminder**

Make sure you've already set up your environment and obtained your TMDB API key. If you haven't done so yet, you might want to refer back to Part 1 of this series, where we cover creating the .env file and configuring your settings to securely load your API key. This setup is essential for accessing live movie data throughout the entire series.

## Next Steps

To follow along with each stage of the project, simply use git checkout to switch to the corresponding branch (e.g., part-2, part-3, etc.).


