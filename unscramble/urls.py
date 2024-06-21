from django.urls import path
from . import views

urlpatterns = [
    path('', views.unscramble_view, name='unscramble'),
]