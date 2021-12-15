from django.db import models
from django.contrib.auth.models import User



class Account(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50, blank=True)
	joined = models.DateTimeField(auto_now_add=True)

	def profile_photos(self):
		return self.photo_set.all()

	def __str__(self):
		return str(self.user)
