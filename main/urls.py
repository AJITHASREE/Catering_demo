"""
URL configuration for main app
"""
from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('menu/', views.menu, name='menu'),
    path('gallery/', views.gallery, name='gallery'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('book-now/', views.book_now, name='book_now'),
    
    # API endpoints
    path('api/submit-booking/', views.submit_booking, name='submit_booking'),
    path('api/submit-contact/', views.submit_contact, name='submit_contact'),
]