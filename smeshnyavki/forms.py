#тут мы будем прописывать модели формы
from .models import *
from django.forms import *


class AddMemForm(Form):
    title = CharField(max_length=255, label='Заголовочек')
    slug = SlugField(max_length=255, label='Адресок в поисковой строчечке')
    content = CharField(widget=Textarea(attrs={'cols':60, 'rows':10}), label='Текстик')
    is_published = BooleanField(label='Публикация', required=False, initial=True)
    categ = ModelChoiceField(queryset=Category.objects.all(), label='Категория котика', empty_label='жмякни на меня')


