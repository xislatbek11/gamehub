from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Application, Category

def app_list(request):
    apps = Application.objects.filter(is_active=True).order_by('-created_at')
    categories = Category.objects.all()
    
    # Filter by category
    category_id = request.GET.get('category')
    if category_id:
        apps = apps.filter(category_id=category_id)
    
    # Search functionality
    search_query = request.GET.get('search')
    if search_query:
        apps = apps.filter(name__icontains=search_query)
    
    # Pagination
    paginator = Paginator(apps, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'apps': page_obj,
        'categories': categories,
        'current_category': category_id,
        'search_query': search_query,
    }
    return render(request, 'apps/app_list.html', context)

def app_detail(request, app_id):
    app = get_object_or_404(Application, id=app_id, is_active=True)
    related_apps = Application.objects.filter(category=app.category, is_active=True).exclude(id=app.id)[:4]
    
    context = {
        'app': app,
        'related_apps': related_apps,
    }
    return render(request, 'apps/app_detail.html', context)

def featured_apps(request):
    apps = Application.objects.filter(is_featured=True, is_active=True).order_by('-rating')
    context = {
        'apps': apps,
        'title': 'Featured Applications'
    }
    return render(request, 'apps/featured_apps.html', context)
