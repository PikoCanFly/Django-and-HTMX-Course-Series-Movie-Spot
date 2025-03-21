﻿# Movie Spot - Part-3: Dynamic Content Loading (asynchronous page loading)




[Watch the Movie Spot Tutorial on YouTube](https://youtu.be/OvaAIpQKXRs)  
<br/>
[![Movie Spot - Part-2 Thumbnail](https://img.youtube.com/vi/OvaAIpQKXRs/hqdefault.jpg)](https://youtu.be/OvaAIpQKXRs)


Welcome to **Movie Spot Part 3**! In this branch, we enhance our Django application by integrating HTMX to enable dynamic, real-time content updates. Building on the foundation from Parts 1 and 2, this branch focuses on updating the landing page dynamically—fetching movie data via the TMDB API, using partial templates, and implementing efficient error handling.

## What's New in Part 3?

- **HTMX Integration:**  
  - Add HTMX to your Django project to enable AJAX-style partial updates without full page reloads.
  
- **Partial Templates:**  
  - Refactor your movie list rendering into a dedicated partial template.
  - Use Django’s `{% include %}` tag to seamlessly insert partials into your main templates.

- **Dynamic GET Requests:**  
  - Utilize HTMX attributes (`hx-get`, `hx-target`, `hx-swap`) to trigger dynamic GET requests to the TMDB API.
  - Render the fetched movie data in real time on your landing page.

- **Error Handling:**  
  - Implement try/except blocks to gracefully manage API request failures.
  - Display user-friendly error messages when issues arise.

- **Enhanced User Experience:**  
  - Improve the responsiveness of your landing page by dynamically loading and updating content.
  - Set the stage for future features like infinite scrolling and live search.
---

## How to Clone and Access Branches

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


**Environment Setup & API Key Reminder**

Make sure you've already set up your environment and obtained your TMDB API key. If you haven't done so yet, you might want to refer back to Part 1 of this series, where we cover creating the .env file and configuring your settings to securely load your API key. This setup is essential for accessing live movie data throughout the entire series.


## Next Steps

To follow along with each stage of the project, simply use git checkout to switch to the corresponding branch (e.g., part-2, part-3, etc.).


