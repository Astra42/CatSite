from django.db.models import Count
from django.core.cache import cache
from .models import *

MENU = [{"title": "About", "url_name": "about"},
        {"title": "Add", "url_name": "add_page"},
        {"title": "Feed Back", "url_name": "contact"},
]

class DataMixin:
        paginate_by = 3

        def get_user_context(self, **kwargs):
                context = kwargs

                categs = cache.get('categs')
                if (not categs):
                    categs = Category.objects.annotate(Count('smeshnyavkа')).order_by('pk')
                    cache.set('categs', categs, 60)

                user_menu = MENU.copy()
                if(not self.request.user.is_authenticated):
                        user_menu.pop(1)

                context['menu'] = user_menu
                context['categs'] = categs
                if('categ_selected' not in context):
                        context['categ_selected'] = 0
                return context