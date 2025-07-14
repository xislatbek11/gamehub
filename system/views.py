from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import SystemTool

def system_list(request):
    tools = SystemTool.objects.filter(is_active=True).order_by('-created_at')
    
    # Filter by category
    category = request.GET.get('category')
    if category:
        tools = tools.filter(category=category)
    
    # Search functionality
    search_query = request.GET.get('search')
    if search_query:
        tools = tools.filter(name__icontains=search_query)
    
    # Pagination
    paginator = Paginator(tools, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # Get unique categories for filter
    categories = SystemTool.objects.values_list('category', flat=True).distinct()
    
    context = {
        'tools': page_obj,
        'categories': categories,
        'current_category': category,
        'search_query': search_query,
    }
    return render(request, 'system/system_list.html', context)

def system_detail(request, tool_id):
    tool = get_object_or_404(SystemTool, id=tool_id, is_active=True)
    related_tools = SystemTool.objects.filter(category=tool.category, is_active=True).exclude(id=tool.id)[:4]
    
    context = {
        'tool': tool,
        'related_tools': related_tools,
    }
    return render(request, 'system/system_detail.html', context)

def featured_tools(request):
    tools = SystemTool.objects.filter(is_featured=True, is_active=True).order_by('-rating')
    context = {
        'tools': tools,
        'title': 'Featured System Tools'
    }
    return render(request, 'system/featured_tools.html', context)
