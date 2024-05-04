from rest_framework import serializers
from .models import Movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['title', 'year', 'duration', 'rated_as', 'genre', 'director', 'rating', 'stars', 'streaming_on']
