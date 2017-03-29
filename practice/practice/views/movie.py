from django.http import HttpResponse
import json
import requests
# from django.template import loader
from django.shortcuts import render




def movie(request):
    search = request.GET.get('search')

    url = "https://watcha.net/home/news.json?page=1&per50"
    response = requests.get(url)
    content = json.loads(response.content)

    movie_items_list = content.get("news")

    if search:
        movie_items_list = list(filter(
                lambda movie: search in movie.get("content"),
                movie_items_list,
                ))

    return render(
            request,
            "movie.html", 
            {"posts_list": movie_items_list,},
            )
