# тут мы будем прописывать модели формы
from captcha.fields import CaptchaField
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import *
from django.forms import *


# 14 Форма, не связанная с моделью
# class AddMemFormCate(Form):
# #     title = CharField(max_length=255, label='Заголовочек')
# #     slug = SlugField(max_length=255, label='Адресок в поисковой строчечке')
# #     content = CharField(widget=Textarea(attrs={'cols':60, 'rows':10}), label='Текстик')
# #     is_published = BooleanField(label='Публикация', required=False, initial=True)
# #     categ = ModelChoiceField(queryset=gory.objects.all(), label='Категория котика', empty_label='жмякни на меня')

# унаследуем от ModelForm
class AddMemForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['categ'].empty_label = 'Жмякни на категорию'

    def clean_title(self):  # пользовательский валидатор
        title = self.cleaned_data['title']
        if (len(title) > 200):
            raise ValidationError('длина префикса больше 200 букавок')
        return title

    class Meta:
        model = Smeshnyavkа  # связь этой формы с моделью
        fields = ['title', 'slug', 'content', 'photo', 'is_published', 'categ']  # какие поля отображать

        widgets = {
            'title': TextInput(attrs={'class': 'form-input'}),
            'content': Textarea(attrs={'cols': 40, 'rows': 20}),
        }
class RegisterUserForm(UserCreationForm):
    username = CharField(label='Логин', widget=TextInput(attrs={'class': 'form-input'}))
    password1 = CharField(label='Пароль', widget=PasswordInput(attrs={'class': 'form-input'}))
    password2 = CharField(label='Повтор пароля', widget=PasswordInput(attrs={'class': 'form-input'}))
    email = EmailField(label='Email', widget=EmailInput(attrs={'class': 'form-input'}))
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):#виджет показывает, как это поле будет отображаться в браузере
    username = CharField(label='Логин', widget=TextInput(attrs={'class': 'form-input'}))# в атрибутах у нас стили
    password = CharField(label='Пароль', widget=PasswordInput(attrs={'class': 'form-input'}))


class ContactForm(forms.Form):
    name = CharField(label='Имя', max_length=255)
    email = EmailField(label='Email')
    content = CharField(widget=Textarea(attrs={'cols':30, 'rows':10}))
    captcha = CaptchaField(label='Вы котик или роботик??')