from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

from .models import Account


@receiver(post_save, sender=User)
def post_save_add_user(sender, created, instance, **kwargs):
	if created:
		Account.objects.create(user=instance)