from django.urls import path
from . import views

app_name = 'system'

urlpatterns = [
    path('', views.system_list, name='system_list'),
    path('featured/', views.featured_tools, name='featured_tools'),
    path('<int:tool_id>/', views.system_detail, name='system_detail'),
] 