from django.db.models import *

# Create your models here.

#поле id уже прописано в стандартом классе model
class Smeshnyavkа(Model):
    title = CharField(max_length=255, verbose_name="заголовок")
    content = TextField(blank=True, verbose_name="текст")#данное поле может быть пустым
    photo = ImageField(upload_to="photo/%Y/%m/%d/", verbose_name="фото")
    pub_time = DateTimeField(auto_now_add=True, verbose_name="дата публикации")
    is_published = BooleanField(default=True,  verbose_name="Публикация")
    categ = ForeignKey('Category', on_delete=PROTECT, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Смешные котики"
        verbose_name_plural = "Смешные котики"
        ordering = ['pub_time', 'title']



class Category(Model):
    name = CharField(max_length=100, db_index=True, verbose_name="Категория")#автоматом добавляется индекс

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ['id']


