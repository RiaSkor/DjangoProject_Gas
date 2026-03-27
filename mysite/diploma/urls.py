from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_chapter, name='add_chapter'),
    path('list/', views.chapter_list, name='chapter_list'),
    path('edit/<int:pk>/', views.edit_chapter, name='edit_chapter'),
    path('delete/<int:pk>/', views.delete_chapter, name='delete_chapter'),
]
