from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Driver

def driver_list(request):
    drivers = Driver.objects.filter(is_active=True).order_by('-created_at')
    
    # Filter by device type
    device_type = request.GET.get('device_type')
    if device_type:
        drivers = drivers.filter(device_type=device_type)
    
    # Filter by manufacturer
    manufacturer = request.GET.get('manufacturer')
    if manufacturer:
        drivers = drivers.filter(manufacturer=manufacturer)
    
    # Search functionality
    search_query = request.GET.get('search')
    if search_query:
        drivers = drivers.filter(name__icontains=search_query)
    
    # Pagination
    paginator = Paginator(drivers, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # Get unique device types and manufacturers for filter
    device_types = Driver.objects.values_list('device_type', flat=True).distinct()
    manufacturers = Driver.objects.values_list('manufacturer', flat=True).distinct()
    
    context = {
        'drivers': page_obj,
        'device_types': device_types,
        'manufacturers': manufacturers,
        'current_device_type': device_type,
        'current_manufacturer': manufacturer,
        'search_query': search_query,
    }
    return render(request, 'drivers/driver_list.html', context)

def driver_detail(request, driver_id):
    driver = get_object_or_404(Driver, id=driver_id, is_active=True)
    related_drivers = Driver.objects.filter(device_type=driver.device_type, is_active=True).exclude(id=driver.id)[:4]
    
    context = {
        'driver': driver,
        'related_drivers': related_drivers,
    }
    return render(request, 'drivers/driver_detail.html', context)

def featured_drivers(request):
    drivers = Driver.objects.filter(is_featured=True, is_active=True).order_by('-rating')
    context = {
        'drivers': drivers,
        'title': 'Featured Drivers'
    }
    return render(request, 'drivers/featured_drivers.html', context)
