from django.db import models

# Create your models here.

class BaseSettings(models.Model):
	title = models.CharField(
		max_length=255,
		verbose_name='Заголовок сайта'
	)
	logo = models.ImageField(
		upload_to='logo/',
		verbose_name='Логотип'	
	)
	facebook = models.URLField(
		verbose_name='Ссылка, на facebook'
	)
	instagram = models.URLField(
		verbose_name='Ссылка, на instagram'
	)
	twitter = models.URLField(
		verbose_name='Ссылка, на twitter'
	)
	github = models.URLField(
		verbose_name='Ссылка, на github'
	)
	google = models.URLField(
		verbose_name='Ссылка, на google'
	)

	def __str__(self):
		return self.title
	
	class Meta:
		verbose_name = 'Настройки'
		verbose_name_plural = 'Настройки'
		