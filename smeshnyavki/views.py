from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, FormView

from smeshnyavki.forms import *
from smeshnyavki.models import *
from .utils import *


# аналог индекса
class CatHome(DataMixin, ListView):
    model = Smeshnyavkа # атрибут, который будет ссылаться на модель
    template_name = "smeshnyavki/index.html"
    context_object_name = 'memes'
    # extra_context = {'title': 'Главная страница'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)#формируется на основе базового класса ListView
        c_def = self.get_user_context(title="Главная страница")# формируется на основе Mixina
        return dict(list(context.items()) + list(c_def.items()))

    # вовзратить то, что должно быть прочитано из модели в переменной model
    def get_queryset(self):#читаем не все, а те, которые опубликованы
        return Smeshnyavkа.objects.filter(is_published=True).select_related('categ')

# def index(request):
#     posts = Smeshnyavkа.objects.all()
#     categs = Category.objects.all()
#
#     conext = {'posts': posts,
#               'categs': categs,
#               'title': 'Главная страничка..',
#               'categ_selected': 0,
#               "menu": MENU}
#     return render(request, "smeshnyavki/index.html", conext)

def about(request):
    contact_list = Smeshnyavkа.objects.all()
    paginator = Paginator(contact_list, 3)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'smeshnyavki/about.html', {'page_obj': page_obj, 'menu': MENU, 'title': 'О сайте'})

#@login_required
class ContactFormView(DataMixin, FormView):
    form_class = ContactForm
    template_name = 'smeshnyavki/contact.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Обратная связь")
        return dict(list(context.items()) + list(c_def.items()))
    def form_valid(self, form):
        print(form.cleaned_data)
        return redirect('home')


class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddMemForm
    template_name = 'smeshnyavki/addpage.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('home')#'/admin/'
    raise_exception = True
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавление мемаса")
        return dict(list(context.items())+list(c_def.items()))
# def addPage(request):
#     if request.method == 'POST':
#         form = AddMemForm(request.POST, request.FILES)
#         if form.is_valid():
#             # print(form.cleaned_data)
#             # try:
#             # Smeshnyavkа.objects.create(**form.cleaned_data)
#             form.save()
#             return (redirect('home'))
#             # except:
#             #     form.add_error(None, 'Ошибка добавления постика')
#     else:
#         form = AddMemForm()
#     conext = {'title': 'О сайтике..', "menu": MENU}
#     return render(request, "smeshnyavki/addpage.html", {'form': form, 'menu': MENU, 'title': 'Добавление мемчика'})


def contact(request):
    conext = {'title': 'О сайтике..', "menu": MENU}
    return render(request, "smeshnyavki/about.html", conext)


# def login(request):
#     conext = {'title': 'О сайтике..', "menu": MENU}
#     return render(request, "smeshnyavki/about.html", conext)

class ShowMem(DataMixin, DetailView):
    model = Smeshnyavkа
    template_name = 'smeshnyavki/mem.html'
    slug_url_kwarg = 'mem_slug'# по дефолту - просто slug
    #pk_url_kwarg = 'post_pk'
    context_object_name = 'mem'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['mem'])
        return dict(list(context.items())+list(c_def.items()))



# def show_mem(request, mem_slug):
#     mem = get_object_or_404(Smeshnyavkа, slug=mem_slug)
#
#     context = {
#         'mem': mem,
#         'menu': MENU,
#         'categ_selected': mem.categ.pk,
#     }
#
#     return (render(request, 'smeshnyavki/mem.html', context))

class CatCategory(DataMixin, ListView):
    model = Smeshnyavkа
    template_name = 'smeshnyavki/index.html'
    context_object_name = 'memes'
    allow_empty = False

    def get_queryset(self):
        print(Smeshnyavkа.objects.filter(categ__slug=self.kwargs['categ_slug'], is_published=True))
        return Smeshnyavkа.objects.filter(categ__slug=self.kwargs['categ_slug'], is_published=True).select_related('categ')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c = Category.objects.get(slug=self.kwargs['categ_slug'])
        c_def = self.get_user_context(
            title=('Категория - ' + str(c.name)),
            categ_selected=c.pk,
        )
        return dict(list(context.items())+list(c_def.items()))

# def show_category(request, catid):
#     posts = Smeshnyavkа.objects.filter(categ_id=catid)
#     categs = Category.objects.all()
#     context = {
#         'posts': posts,
#         'categs': categs,
#         'menu': MENU,
#         'title': "Main page",
#         'categ_selected': catid,
#     }
#     return render(request, 'smeshnyavki/index.html', context)


# def categories(request, memid):
#     if (int(memid) == 1):
#         return redirect('home')
#
#     return HttpResponse(f'нига стаки блеки о {memid}')
class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'smeshnyavki/register.html'
    success_url = reverse_lazy('login')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация')
        return dict(list(context.items()) + list(c_def.items()))
    def form_valid(self, form):#вызывается при успешной проверке формы регистрации
        user = form.save()#добавляем пользователя в бд
        login(self.request, user)
        return redirect('home')

class loginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'smeshnyavki/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Авторизиация')
        return dict(list(context.items()) + list(c_def.items()))
    # def get_success_url(self):
    #     return reverse_lazy('home')
    # Прописали в константах

def logout_user(request):
    logout(request)
    return redirect('login')

def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1> котики такую страницу не нашли( <h1>")
