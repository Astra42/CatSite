# Generated by Django 3.2.14 on 2022-08-08 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smeshnyavki', '0002_auto_20220807_0002'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['id'], 'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='smeshnyavkа',
            options={'ordering': ['pub_time', 'title'], 'verbose_name': 'Смешные котики', 'verbose_name_plural': 'Смешные котики'},
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(db_index=True, max_length=100, verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='smeshnyavkа',
            name='content',
            field=models.TextField(blank=True, verbose_name='текст'),
        ),
        migrations.AlterField(
            model_name='smeshnyavkа',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='Публикация'),
        ),
        migrations.AlterField(
            model_name='smeshnyavkа',
            name='photo',
            field=models.ImageField(upload_to='photo/%Y/%m/%d/', verbose_name='фото'),
        ),
        migrations.AlterField(
            model_name='smeshnyavkа',
            name='pub_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='дата публикации'),
        ),
        migrations.AlterField(
            model_name='smeshnyavkа',
            name='title',
            field=models.CharField(max_length=255, verbose_name='заголовок'),
        ),
    ]
