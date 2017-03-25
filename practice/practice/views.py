from django.http import HttpResponse
from django.conf import settings
import json
import requests


def home(request):
    return HttpResponse("hello world")


def room(request, room_id):
    url = "https://api.zigbang.com/v1/items?detail=true&item_ids=" + room_id
    response = requests.get(url)

    return HttpResponse(response.content)


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

    with open(settings.BASE_DIR + "/practice/templates/movie.html", "r") as template:
        content = template.read()
        count = len(movie_items_list)

        movie_content = "<h1> movie page </h1>" +\
                        "".join([
                        "<h3>{title}</h3><img src={img_src} alt={title}><p>{content}</p>".format(
                            title=movie.get('title'),
                            img_src=movie.get('image'),
                            content=movie.get('content'),
                           )
                            for movie
                            in movie_items_list
                                ])

    content = content.replace("## count ##", str(count))
    content = content.replace("## movie_content ##", movie_content)

    return HttpResponse(content)
