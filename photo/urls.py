from django.urls import path

from . import views

app_name = 'photo'

urlpatterns = [
	path('', views.index, name='index'),
	path('about/', views.about, name='about'),
	path('contact/', views.contact, name='contact'),
	path('single/<int:id>', views.single, name='single'),
	
	path('create_photo/', views.create_photo, name='create-photo'),
	path('update/<int:id>', views.update_photo, name='update-photo'),
	path('delete/<int:id>', views.delete_photo, name='delete-photo'),

	path('create_category/', views.category_cre, name='category-create')

]