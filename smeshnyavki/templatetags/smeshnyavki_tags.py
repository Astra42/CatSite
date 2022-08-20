from django import template
from smeshnyavki.models import *

#экземпляр класса library для регистрации тегов
register = template.Library()
#simple tag
@register.simple_tag(name='getCategs')#function is changed into tage
def get_categories(filter=None):
    if filter:
        return Category.objects.filter(pk=filter) #возвращаем коллекцию
    return Category.objects.all() #возвращаем коллекцию

@register.inclusion_tag('smeshnyavki/list_categories.html')
def show_categories(sort=None, categ_selected=0):
    categs = Category.objects.all() #возвращаем коллекцию
    if sort:
        categs = Category.objects.order_by(sort) #возвращаем коллекцию
    return{"categs": categs, 'categ_selected': categ_selected}
