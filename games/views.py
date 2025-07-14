from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Game

def game_list(request):
    games = Game.objects.filter(is_active=True).order_by('-created_at')
    
    # Filter by genre
    genre = request.GET.get('genre')
    if genre:
        games = games.filter(genre=genre)
    
    # Search functionality
    search_query = request.GET.get('search')
    if search_query:
        games = games.filter(name__icontains=search_query)
    
    # Pagination
    paginator = Paginator(games, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # Get unique genres for filter
    genres = Game.objects.values_list('genre', flat=True).distinct()
    
    context = {
        'games': page_obj,
        'genres': genres,
        'current_genre': genre,
        'search_query': search_query,
    }
    return render(request, 'games/game_list.html', context)

def game_detail(request, game_id):
    game = get_object_or_404(Game, id=game_id, is_active=True)
    related_games = Game.objects.filter(genre=game.genre, is_active=True).exclude(id=game.id)[:4]
    
    context = {
        'game': game,
        'related_games': related_games,
    }
    return render(request, 'games/game_detail.html', context)

def featured_games(request):
    games = Game.objects.filter(is_featured=True, is_active=True).order_by('-rating')
    context = {
        'games': games,
        'title': 'Featured Games'
    }
    return render(request, 'games/featured_games.html', context)
