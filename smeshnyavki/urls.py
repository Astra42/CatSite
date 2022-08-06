from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('mem/<slug:memid>', categories),
    path('about/', about, name='about'),
]
