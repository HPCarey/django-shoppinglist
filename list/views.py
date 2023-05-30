from django.shortcuts import render, redirect
from .models import List, Item
from .forms import ListForm, ItemForm
from django.db.models import F


def index(request):
    lists = List.objects.filter(user=request.user)
    form = ListForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            save = form.save(commit=False)
            save.user = request.user
            save.save()
    context = {
        'lists': lists,
        'form': form
    }
    return render(request, 'index.html', context)


def list(request, id):
    list = List.objects.get(id=id)

    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.list = list
            item.save()
            return redirect('list', id=id)
    else:
        form = ItemForm()
    context = {
        'list': list,
        'form': form
    }
    return render(request, 'list.html', context)
