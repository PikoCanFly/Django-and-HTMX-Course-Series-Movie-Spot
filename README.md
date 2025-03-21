﻿﻿# Movie Spot - Part-4: Dynamic Content Loading (asynchronous page loading)




[Watch the Movie Spot Tutorial on YouTube](https://youtu.be/qR69hcoOi3s)  
<br/>
[![Movie Spot - Part-2 Thumbnail](https://img.youtube.com/vi/qR69hcoOi3s/hqdefault.jpg)](https://youtu.be/qR69hcoOi3s)


Welcome to **Movie Spot Part 4**!  In this branch, we implement infinite scrolling to dynamically load additional movie data on your landing page. Building on the foundation from earlier parts, you'll learn how to:

- **Implement Infinite Scrolling with HTMX:**  
  Detect when users reach the bottom of the page and automatically fetch more movie data from the TMDB API without a full page refresh.

- **Use Partial Templates:**  
  Refactor your movie list into a partial template that can be dynamically appended to the page.

- **Enhance User Experience:**  
  Create a seamless, modern interface that updates in real time using HTMX attributes (`hx-get`, `hx-target`, `hx-swap`).


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


