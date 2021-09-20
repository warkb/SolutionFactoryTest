from datetime import datetime
from django.db import models
from django.contrib.auth.models import User, Group 


class Poll(models.Model):
	name = models.CharField("Название", max_length=300)
	description = models.CharField("Описание", max_length=300)
	start_date = models.DateTimeField("Дата начала", default=datetime.now, editable=False)
	end_date = models.DateTimeField("Дата окончания	")
	def __str__(self):
		return self.name

class Question(models.Model):
	question_types = [(0, 'Текст'),(1, 'Один вариант'),(2, 'Несколько вариантов')]
	poll = models.ForeignKey(Poll, related_name='questions', on_delete=models.CASCADE, verbose_name='Опрос')
	text = models.CharField("Название", max_length=300)
	question_type = models.PositiveIntegerField("Тип вопроса", choices=question_types)
	def __str__(self):
		return self.text

class AnswerOption(models.Model):
	variant = models.CharField("Вариант ответа", max_length=300)
	question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='Вопрос')
	def __str__(self):
		return self.variant

class Answer(models.Model):
	text = models.CharField("Текст ответа", max_length=300, null=True, blank=True)
	variants = models.ManyToManyField(AnswerOption, verbose_name='Выбранные варианты')
	user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь',  null=True)
	question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='Вопрос')