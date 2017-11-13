from django.db import models

# Create your models here.

from django.conf import settings

class Profile(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
	photo = models.ImageField(upload_to = 'users/%Y/%m/%d', blank = True)
	date_of_birth = models.DateField(blank = True, null = True)
	def __str__(self):
		return 'Profile for user {}'.format(self.user.username)
