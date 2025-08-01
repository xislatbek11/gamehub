# Generated by Django 5.2.4 on 2025-07-12 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('version', models.CharField(max_length=20)),
                ('file', models.FileField(upload_to='drivers/')),
                ('icon', models.ImageField(blank=True, null=True, upload_to='driver_icons/')),
                ('screenshot', models.ImageField(blank=True, null=True, upload_to='driver_screenshots/')),
                ('device_type', models.CharField(max_length=100)),
                ('manufacturer', models.CharField(max_length=100)),
                ('developer', models.CharField(max_length=100)),
                ('size', models.CharField(max_length=20)),
                ('downloads', models.IntegerField(default=0)),
                ('rating', models.DecimalField(decimal_places=2, default=0.0, max_digits=3)),
                ('is_featured', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
