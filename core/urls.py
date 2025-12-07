from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact_view, name='contact'),
    path('sitemap.xml', views.sitemap_view, name='sitemap'),
]
