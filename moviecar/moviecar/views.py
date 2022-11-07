from django.shortcuts import render

from .models import Movie

def index(req):
    movie_list = Movie.objects.all()
    context = {
        'movie_list' : movie_list,
    }
    return render(req, 'index.html', context)

def detail(req, movie_id):
    try:
        movie = Movie.objects.get(pk=movie_id)
    except Movie.DoesNotExist:
        raise Http404("Movie does not exist")
    return render(req, 'movie.html', {'movie': movie})