from django.db import models

# Create your models here.
from django.conf import settings
from django.utils.text import slugify
from django.urls import reverse

class Image(models.Model):
	#image的属性:
	title = models.CharField(max_length = 200)
	slug = models.SlugField(max_length = 200, blank = True)
	url = models.URLField()
	image = models.ImageField(upload_to = 'images/%Y/%m/%d')
	description = models.TextField(blank = True)
	created = models.DateTimeField(auto_now_add = True, db_index = True)
	#image的所有者:
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, related_name = 'images_created')
	#image的喜欢者:
	user_like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name = 'images_liked', blank = True)
	
	def __str__(self):
		return self.title
	def save(self, *args, **kw):
		if not self.slug:
			self.slug = slugify(self.title)
			super(Image, self).save(*args, **kw)
	def get_absolute_url(self):
		return reverse('images:detail', args = (self.id, self.slug))
