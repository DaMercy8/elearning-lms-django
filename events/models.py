from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Event(models.Model):
	name = models.CharField(max_length=200, blank=True, null=True)
	theme_or_sub = models.CharField(max_length=200, blank=True, null=True)
	description = models.CharField(max_length=200, blank=True, null=True)
	date = models.DateField(default=False)
	location = models.CharField(max_length=200, blank=True, null=True)
	image = models.ImageField(null=True, blank=True)




	def __str__(self):
		return self.name

	@property
	def imageURL(self):
		try:
			url = self.image.url
		except:
			url = ''
		return url