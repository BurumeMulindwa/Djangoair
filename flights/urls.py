from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('flight/<int:flight_id>/', views.flight, name='flight'),
    path('book/<int:flight_id>/', views.book, name='book'),
]
