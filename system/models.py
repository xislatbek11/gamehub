from django.db import models

# Create your models here.

class SystemTool(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    version = models.CharField(max_length=20)
    file = models.FileField(upload_to='system_tools/')
    icon = models.ImageField(upload_to='system_icons/', blank=True, null=True)
    screenshot = models.ImageField(upload_to='system_screenshots/', blank=True, null=True)
    category = models.CharField(max_length=100)
    developer = models.CharField(max_length=100)
    size = models.CharField(max_length=20)
    downloads = models.IntegerField(default=0)
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)
    is_featured = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
