from django.urls import path
from django.urls import path, include
from movies.views import upload_file_view, upload_success, base_view

urlpatterns = [
    path('', base_view, name='base'),
    path('upload/', upload_file_view, name='upload_file'),
    path('upload/success/', upload_success, name='upload_success'),
    path('explore/', include('movie_explorer.urls')),
]
