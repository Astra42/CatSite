from django.db import models

# Create your models here.

#поле id уже прописано в стандартом классе model
class Smeshnyavkа(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)#данное поле может быть пустым
    photo = models.ImageField(upload_to="photo/%Y/%m/%d/")
    pub_time = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title


