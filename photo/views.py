from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import Category, Photo
from .forms import PhotoForm, CategoryForm
from accounts.models import Account

def index(request):
	category = Category.objects.all()
	context = {'category':category}
	return render(request, 'index.html', context)


def about(request):
	return render(request, 'about.html')

def contact(request):
	return render(request, 'contact.html')


def single(request, id):
	categories = get_object_or_404(Category, id=id)
	
	photos = Photo.objects.filter(category=categories, featured=True)

	# photos = Photo.objects.filter(featured=True)

	context = {
	'categories':categories,
	'photos':photos
	}
	return render(request, 'single.html', context)

@login_required
def create_photo(request):
	author  = Account.objects.get(user=request.user) 
	form = PhotoForm(request.POST or None, request.FILES or None)
	created = False
	if request.method == 'POST':
		if form.is_valid():
			form.instance.author = author
			form.save()
			created = True
			return redirect('user-page')
	context = {
	'form': form
	}
	return render(request, 'photo/create_photo.html', context)
@login_required
def category_cre(request):
	form = CategoryForm(request.POST, request.FILES)
	if request.method == 'POST':
		if form.is_valid():
			form.save()
		return redirect('photo:index')
	return render(request, 'photo/category_cre.html', {'form':form})

@login_required
def update_photo(request,id):
	photo = get_object_or_404(Photo, id=id)
	author = Account.objects.get(user=request.user)
	form  = PhotoForm(
		request.POST or None,
		request.FILES or None,
		instance=photo) 
	if request.method == 'POST':
		if form.is_valid():
			form.instance.author = author
			form.save()
			return redirect('user-page')
	context = {'form':form}
	return render(request, 'photo/update_photo.html', context)

@login_required
def delete_photo(request, id):
	objects = get_object_or_404(Photo, id=id)
	objects.delete()
	return redirect('user-page')