from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.contrib import messages
from django.urls import reverse
from .models import URL
from .forms import URLForm

def home(request):
    if request.method == 'POST':
        form = URLForm(request.POST)
        if form.is_valid():
            url_obj = form.save()
            short_url = request.build_absolute_uri(reverse('redirect_url', args=[url_obj.short_code]))
            return render(request, 'success.html', {
                'original_url': url_obj.original_url,
                'short_url': short_url,
                'short_code': url_obj.short_code
            })
    else:
        form = URLForm()
    
    return render(request, 'home.html', {'form': form})

def redirect_url(request, short_code):
    url_obj = get_object_or_404(URL, short_code=short_code)
    url_obj.click_count += 1
    url_obj.save()
    return redirect(url_obj.original_url)

def stats_view(request, short_code):
    url_obj = get_object_or_404(URL, short_code=short_code)
    return render(request, 'stats.html', {'url': url_obj})

def api_shorten(request):
    if request.method == 'POST':
        original_url = request.POST.get('url')
        if original_url:
            if not original_url.startswith(('http://', 'https://')):
                original_url = 'https://' + original_url
            
            url_obj = URL.objects.create(original_url=original_url)
            short_url = request.build_absolute_uri(reverse('redirect_url', args=[url_obj.short_code]))
            
            return JsonResponse({
                'success': True,
                'short_url': short_url,
                'original_url': original_url,
                'short_code': url_obj.short_code
            })
    
    return JsonResponse({'success': False, 'error': 'Invalid request'})