from django.urls import path
from . import views

app_name = 'apps'

urlpatterns = [
    path('', views.app_list, name='app_list'),
    path('featured/', views.featured_apps, name='featured_apps'),
    path('<int:app_id>/', views.app_detail, name='app_detail'),
] 