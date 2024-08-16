from django.shortcuts import render
from . import models

def banner_view(request):
    banners = models.Banner.objects.filter(is_active = True)[:5]
    
    context = {}
    context['banners'] = banners

    return render(request, 'index.html', context)

