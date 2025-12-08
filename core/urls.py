from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact_view, name='contact'),
    path('feedback/', views.feedback_view, name='feedback'),
    path('sitemap.xml', views.sitemap_view, name='sitemap'),
]
