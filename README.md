# Movie Spot - Part-2: Dynamic Landing Page & Live Data Integration




[Watch the Movie Spot Tutorial on YouTube](https://youtu.be/uWfIoc-d0H4)  
<br/>
[![Movie Spot - Part-2 Thumbnail](https://img.youtube.com/vi/uWfIoc-d0H4/hqdefault.jpg)](https://youtu.be/uWfIoc-d0H4)


In this part of the tutorial, we enhance our Django project by creating a dynamic landing page that integrates live movie data from the TMDB API. Building on the foundation set in Part-1, Part-2 introduces the following features:

- **Secure API Key Management:**  
  - Obtain your free TMDB API key.  
  - Create a `.env` file and configure Django to load environment variables securely using python-dotenv.

- **Dynamic Landing Page:**  
  - Build a Django view that fetches movie data from the TMDB API based on user-selected criteria (category or search term).  
  - Use Python's `requests` library to send HTTP requests and retrieve live data.

- **Interactive Forms & Templating:**  
  - Create and style forms (dropdown and search input) using Django’s templating language and Bootstrap.  
  - Dynamically render movie data in responsive Bootstrap cards.

- **Error Handling:**  
  - Implement robust error handling using try/except blocks to manage API errors gracefully.

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
git checkout part-2
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


