from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('api/shorten/', views.api_shorten, name='api_shorten'),
    path('stats/<str:short_code>/', views.stats_view, name='stats'),
    path('<str:short_code>/', views.redirect_url, name='redirect_url'),
]