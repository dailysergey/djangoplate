from django.db import models

# Create your models here.


class City(models.Model):
	name = models.CharField(max_length=50)
	# blank - means may be null
	slug = models.CharField(max_length=50, blank=True)
	class Meta:
		verbose_name = 'Название неселенного пункта'
		verbose_name_plural = 'Название населенных пунктов'

	def __str__(self):
		return self.name
