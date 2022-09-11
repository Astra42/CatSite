from django.db.models import *

# Create your models here.

#поле id уже прописано в стандартом классе model
class Smeshnyavkа(Model):
    title = CharField(max_length=255, verbose_name="заголовок")
    slug = SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    content = TextField(blank=True, verbose_name="текст")#данное поле может быть пустым
    photo = ImageField(upload_to="photo/%Y/%m/%d/", verbose_name="фото")
    pub_time = DateTimeField(auto_now_add=True, verbose_name="дата публикации")
    is_published = BooleanField(default=True,  verbose_name="Публикация")
    categ = ForeignKey('Category', on_delete=PROTECT,  verbose_name="Категория котика")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Смешные котики"
        verbose_name_plural = "Смешные котики"
        ordering = ['pub_time', 'title']



class Category(Model):
    name = CharField(max_length=100, db_index=True, verbose_name="Категория")#автоматом добавляется индекс
    slug = SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ['pk',]


