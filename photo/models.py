from django.db import models
from django.template.defaultfilters import slugify
from accounts.models import Account



class Category(models.Model):
	name = models.CharField(max_length=100)
	thumbnail = models.ImageField(upload_to='categories/')


	def __str__(self):
		return str(self.name)


class Photo(models.Model):
	title = models.CharField(max_length=100)
	author = models.ForeignKey(Account, on_delete=models.CASCADE)
	category = models.ForeignKey(Category, on_delete=models.CASCADE) 
	image = models.ImageField(upload_to='images/')
	timestamp = models.DateTimeField(auto_now_add=True)
	featured = models.BooleanField(default=False)
	slug = models.SlugField(unique=True, blank=True)

	def __str__(self):
		return f"{self.title[:10]}-{self.author}"

	def save(self, *args, **kwargs):
		if self.slug == '':
			self.slug = slugify(self.title)
		return super().save(*args, **kwargs)

	class Meta:
		ordering = ['-timestamp']

