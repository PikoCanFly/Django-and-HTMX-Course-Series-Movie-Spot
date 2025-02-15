from django.shortcuts import render
from django.conf import settings
import requests

def landing_page(request):
    category = request.GET.get("category", "popular")
    search_query = request.GET.get("search", "")
    API_KEY = settings.TMDB_API_KEY
    page = int(request.GET.get("page", 1))
    next_page = page + 1
    base_url="https://api.themoviedb.org/3/movie/"
    error_message = ""
    if search_query:
        url = f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={search_query}&page={page}"
    else:
        url = f"{base_url}{category}?api_key={API_KEY}&page={page}"
    try:    
        response = requests.get(url)
        response.raise_for_status()
        data = response.json().get('results',[])
        total_pages= response.json().get("total_pages",1)
        has_next = page < total_pages
    except Exception as e:
        data=[]
        error_message= f"Something went wrong!"
        has_next= False

    if request.headers.get("HX-Request"):
        return render(request, "movies/partials/_movie_list.html", {"movies":data, "category":category,
                                                   "search_query":search_query,
                                                   "error_message":error_message,
                                                   "next_page":next_page,
                                                   "has_next":has_next})
        
    return render(request, "movies/landing.html", {"movies":data, "category":category,
                                                   "search_query":search_query,
                                                   "error_message":error_message,
                                                   "next_page":next_page,
                                                   "has_next":has_next})
    
    
    