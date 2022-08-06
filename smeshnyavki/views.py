from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect


# Create your views here.
from smeshnyavki.models import Smeshnyavkа

MENU = ["О сайте", "Об авторе", "Настройки", "Музон"]
def index(request):
    posts = Smeshnyavkа.objects.all()
    conext = {'posts':posts, 'title':'Главная страничка..', "menu":MENU}
    return render(request, "smeshnyavki/index.html", conext)

def about(request):
    conext = {'title':'О сайтике..', "menu":MENU}
    return render(request, "smeshnyavki/about.html", conext)

def categories(request, memid):
    if (int(memid) == 1):
        return redirect('home')

    return HttpResponse(f'нига стаки блеки о {memid}')

def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1> котики такую страницу не нашли( <h1>")