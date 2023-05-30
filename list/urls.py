from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list_items/<int:id>/', views.list, name="list"),
    path('delete_items/<int:id>/', views.deleteItem, name="delete_item"),
    path('complete_items/<int:id>/', views.completeItem, name="complete_item")


]
