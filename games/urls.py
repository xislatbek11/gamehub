from django.urls import path
from . import views

app_name = 'games'

urlpatterns = [
    path('', views.game_list, name='game_list'),
    path('featured/', views.featured_games, name='featured_games'),
    path('<int:game_id>/', views.game_detail, name='game_detail'),
] 