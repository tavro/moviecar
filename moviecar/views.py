from django.shortcuts import render
from .models import Movie


def index(req):
    if req.method == 'POST':
        name = req.POST['name']
        url = req.POST['url']
        movie = Movie.objects.create(title=name, img=url)
        movie.save()

    movie_list = Movie.objects.all()
    context = {
        'movie_list' : movie_list,
    }
    return render(req, 'index.html', context)


def detail(req, movie_id):
    if req.method == 'POST':
        desc = req.POST['review']
        stars = req.POST['rating']
        obj = Movie.objects.get(pk=movie_id)
        obj.review = desc
        obj.rating = int(stars)
        obj.have_watched = True
        obj.save()
    try:
        movie = Movie.objects.get(pk=movie_id)
    except Movie.DoesNotExist:
        raise Http404("Movie does not exist")
    return render(req, 'movie.html', {'movie': movie})


def edit(req, movie_id):
    if req.method == 'POST':
        desc = req.POST['review']
        stars = req.POST['rating']
        obj = Movie.objects.get(pk=movie_id)
        obj.review = desc
        obj.rating = int(stars)
        obj.save()
    try:
        movie = Movie.objects.get(pk=movie_id)
    except Movie.DoesNotExist:
        raise Http404("Movie does not exist")
    return render(req, 'movie_edit.html', {'movie': movie})