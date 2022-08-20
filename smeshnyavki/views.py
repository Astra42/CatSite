from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect


# Create your views here.
from smeshnyavki.models import *

MENU = [{"title":"About", "url_name":"about"},
        {"title":"Add", "url_name":"add_page"},
        {"title":"Feed Back", "url_name":"contact"},
        {"title":"Enter", "url_name":"login"},
        ]

def index(request):
    posts = Smeshnyavkа.objects.all()
    categs = Category.objects.all()

    conext = {'posts':posts,
              'categs':categs,
              'title':'Главная страничка..',
              'categ_selected': 0,
               "menu":MENU}
    return render(request, "smeshnyavki/index.html", conext)

def about(request):
    conext = {'title':'О сайтике..', "menu":MENU}
    return render(request, "smeshnyavki/about.html", conext)

def addPage(request):
    conext = {'title':'О сайтике..', "menu":MENU}
    return render(request, "smeshnyavki/about.html", conext)

def contact(request):
    conext = {'title':'О сайтике..', "menu":MENU}
    return render(request, "smeshnyavki/about.html", conext)

def login(request):
    conext = {'title':'О сайтике..', "menu":MENU}
    return render(request, "smeshnyavki/about.html", conext)

def show_mem(request, memid):
    return(HttpResponse(f"отображение мема номер{memid}"))

def show_category(request, catid):
    posts = Smeshnyavkа.objects.filter(categ_id=catid)
    categs = Category.objects.all()

    context = {
        'posts':posts,
        'categs':categs,
        'menu': MENU,
        'title':"Main page",
        'categ_selected':catid,
    }
    return render(request, 'smeshnyavki/index.html', context)

# def categories(request, memid):
#     if (int(memid) == 1):
#         return redirect('home')
#
#     return HttpResponse(f'нига стаки блеки о {memid}')

def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1> котики такую страницу не нашли( <h1>")