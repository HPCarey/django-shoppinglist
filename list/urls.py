from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list_items/<int:id>/', views.list, name="list")
]
