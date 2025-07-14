from django.urls import path
from . import views

app_name = 'drivers'

urlpatterns = [
    path('', views.driver_list, name='driver_list'),
    path('featured/', views.featured_drivers, name='featured_drivers'),
    path('<int:driver_id>/', views.driver_detail, name='driver_detail'),
] 