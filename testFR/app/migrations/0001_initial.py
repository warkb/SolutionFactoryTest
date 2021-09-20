# Generated by Django 2.2.10 on 2021-09-17 21:14

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AnswerOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('variant', models.CharField(max_length=300, verbose_name='Вариант ответа')),
            ],
        ),
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='Название')),
                ('description', models.CharField(max_length=300, verbose_name='Описание')),
                ('start_date', models.DateTimeField(default=datetime.datetime.now, editable=False, verbose_name='Дата начала')),
                ('end_date', models.DateTimeField(verbose_name='Дата окончания\t')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=300, verbose_name='Название')),
                ('question_type', models.PositiveIntegerField(choices=[(0, 'Текст'), (1, 'Один вариант'), (2, 'Несколько вариантов')], verbose_name='Тип вопроса')),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Poll', verbose_name='Опрос')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(blank=True, max_length=300, null=True, verbose_name='Текст ответа')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
                ('variants', models.ManyToManyField(to='app.AnswerOption', verbose_name='Выбранные варианты')),
            ],
        ),
    ]