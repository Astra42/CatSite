from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('categ/<int:catid>', show_category, name='category'),
    path('mem/<slug:mem_slug>', show_mem, name='mem'),

    path('about/', about, name='about'),
    path('add_page/', addPage, name='add_page'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
]
