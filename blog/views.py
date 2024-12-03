import requests
from django.http import JsonResponse

from django.http import JsonResponse
from .models import BlogPost

def get_blog_posts(request):
    country = request.GET.get('country', None)
    if country:
        posts = BlogPost.objects.filter(country=country)
    else:
        posts = BlogPost.objects.all()

    data = [{'title': post.title, 'content': post.content, 'country': post.country} for post in posts]
    return JsonResponse({'posts': data})


def detect_country(request):
    ip_address = request.META.get('REMOTE_ADDR', '8.8.8.8')  # Default to public IP for testing
    response = requests.get(f"http://ip-api.com/json/{ip_address}")
    data = response.json()
    country = data.get('country', 'US')
    return JsonResponse({'country': country})
