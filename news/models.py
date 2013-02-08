from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
	title = models.CharField(max_length = 30, verbose_name='Заголовок')
	text = models.CharField(max_length = 200, verbose_name='Текст')
	pub_date = models.DateTimeField(verbose_name='Дата')
	author = models.ForeignKey(User)
	class Meta:
		verbose_name = "новость"
		verbose_name_plural = "новости"
		permissions = (
			("can_topic_change", "Изменение и добавление"),
		)

class Comment(models.Model):
	topic = models.ForeignKey(Topic)
	text = models.CharField(max_length = 200)
	pub_date = models.DateTimeField('date published')
	author = models.ForeignKey(User)
	class Meta:
		verbose_name = "комментарий"
		verbose_name_plural = "комментарии"