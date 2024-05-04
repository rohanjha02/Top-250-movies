from django.views.generic import ListView
from django.db.models import Q
from movies.models import Movie
from django.shortcuts import render

class MovieListView(ListView):
    model = Movie
    template_name = 'movie_explorer/movie_list.html'
    context_object_name = 'movies'

    def get_queryset(self):
        query = self.request.GET.get("q")
        if query:
            return Movie.objects.filter(
                Q(title__icontains=query) |
                Q(director__icontains=query) |
                Q(genre__icontains=query)
            )
        else:
            return Movie.objects.all()

# movie_explorer/views.py

from django.views.generic import DetailView

class MovieDetailView(DetailView):
    model = Movie
    template_name = 'movie_explorer/movie_detail.html'
    context_object_name = 'movie'

def base_view(request):
    return render(request, 'base.html')