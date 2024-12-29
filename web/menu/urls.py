# from django.contrib import admin
from django.urls import path
# from django_prometheus import exports
from . import views

app_name = 'menu'
urlpatterns = [
    path('', views.IndexClassView.as_view(), name='index'),
    path('<int:pk>/', views.MenuClassView.as_view(), name='details'), # pk - primary key
    path('add/', views.CreateItemView.as_view(), name='create_item'),
    path('edit/<int:id>', views.edit_item, name='edit_item'),
    path('delete/<int:id>', views.delete_item, name='delete_item'),
]
