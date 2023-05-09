from django.shortcuts import render, get_object_or_404, redirect

from .models import Movie
from .forms import MovieForm

from django.contrib.auth.decorators import login_required

@login_required
def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movies/home.html', {'movies': movies})

@login_required
def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    return render(request, 'movies/movie_detail.html', {'movie': movie})

@login_required
def movie_new(request):
    if request.method == "POST":
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.save()
            return redirect('movie-detail', pk=movie.pk)
    else:
        form = MovieForm()
    return render(request, 'movies/movie_update.html', {'form': form})

@login_required
def movie_edit(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == "POST":
        form = MovieForm(request.POST, request.FILES, instance=movie)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.save()
            return redirect('movie-detail', pk=movie.pk)
    else:
        form = MovieForm(instance=movie)
    return render(request, 'movies/movie_update.html', {'form': form})

@login_required
def movie_delete(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    movie.delete()
    return redirect('movie_list')