from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_list, name='movies-page'),
    path('create/', views.movie_new, name='movie-create'),
    path('<int:pk>/', views.movie_detail, name='movie-detail'),
    path('<int:pk>/update/', views.movie_edit, name='movie-update'),
    path('<int:pk>/delete/', views.movie_delete, name='movie-delete'),
]
