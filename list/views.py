from django.shortcuts import render, redirect
from .models import List, Item


def index(request):
    lists = List.objects.filter(user=request.user)
    context = {
        'lists': lists
    }
    return render(request, 'index.html', context)


def list(request, id):
    list = List.objects.get(id=id)
    context = {
        'list': list
    }
    return render(request, 'list.html', context)
