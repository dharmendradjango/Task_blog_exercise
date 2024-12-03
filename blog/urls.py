from django.urls import path
from . import views

urlpatterns = [
    path('api/detect-country/', views.detect_country, name='detect_country'),
    path('api/blog-posts/', views.get_blog_posts, name='get_blog_posts'),
]
