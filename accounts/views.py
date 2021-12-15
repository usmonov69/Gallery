from django.shortcuts import render
from  itertools import chain 

from .models import Account

def user_page(request):
	account = Account.objects.get(user=request.user)
	photos = []
	my_photos = account.profile_photos()
	photos.append(my_photos)
	print(photos)
	
	if len(photos)>0:
		qs = sorted(chain(*photos), reverse=True, key= lambda obj: obj.timestamp)

	context = {
	'account':account,
	'photos':qs,
	}	
	return render(request, 'profile/user_page.html', context)
