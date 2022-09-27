# Generated by Django 4.1.1 on 2022-09-27 09:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.TextField(blank=True, default=1, max_length=200, null=True, verbose_name='Категория')),
                ('description', models.TextField(blank=True, max_length=3000, null=True, verbose_name='Описание')),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(default='None', max_length=1000, verbose_name='Наименование')),
                ('description', models.TextField(blank=True, max_length=3000, null=True, verbose_name='Описание')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('price', models.DecimalField(decimal_places=0, max_digits=19, verbose_name='Стоимость')),
                ('image', models.ImageField(upload_to='', verbose_name='Изображение')),
                ('category', models.ForeignKey(default=None, on_delete=django.db.models.deletion.RESTRICT, related_name='categories', to='webapp.categories', verbose_name='Категория')),
            ],
        ),
    ]
