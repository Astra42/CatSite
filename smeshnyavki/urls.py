from django.urls import path
from django.views.decorators.cache import cache_page

from .views import *




#
urlpatterns = [
    # path('', index, name='home'),
    path('', CatHome.as_view(), name='home'),
    # path('categ/<int:catid>', show_category, name='category'),
    path('categ/<slug:categ_slug>', CatCategory.as_view(), name='category'),
    path('mem/<slug:mem_slug>', ShowMem.as_view(), name='mem'),
    path('about/', about, name='about'),
    path('add_page/', AddPage.as_view(), name='add_page'),
    path('contact/', ContactFormView.as_view(), name='contact'),
    path('login/', loginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
]
