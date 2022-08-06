from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect


# Create your views here.
from smeshnyavki.models import Smeshnyavkа

MENU = [{"title":"About", "url_name":"about"},
        {"title":"Add", "url_name":"add_page"},
        {"title":"Feed Back", "url_name":"contact"},
        {"title":"Enter", "url_name":"login"},
        ]

def index(request):
    posts = Smeshnyavkа.objects.all()
    conext = {'posts':posts,
              'title':'Главная страничка..',
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

# def categories(request, memid):
#     if (int(memid) == 1):
#         return redirect('home')
#
#     return HttpResponse(f'нига стаки блеки о {memid}')

def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1> котики такую страницу не нашли( <h1>")