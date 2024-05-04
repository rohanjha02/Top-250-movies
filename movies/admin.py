from django.contrib import admin
from .models import Movie

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'director', 'year', 'rating']
    search_fields = ['title', 'director']
    list_filter = ['year', 'genre']
