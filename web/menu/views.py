from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item
from .forms import ItemForm
from foodie.utils import *
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

# Create your views here.
class IndexClassView(ListView):
    model = Item
    template_name = 'menu/index.html'
    context_object_name = 'item_list'

class MenuClassView(DetailView):
    model = Item
    template_name = "menu/details.html"

class CreateItemView(CreateView):
    model = Item
    fields = ["name", "description", "price", "image", "category"]
    template_name = "menu/item-form.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

def create_item(request):
    form = ItemForm(request.POST or None, request.FILES or None)
    
    if form.is_valid():
        form.save()
        return redirect('menu:index')
    
    return render(request, 'menu/item-form.html', {'form': form})

def edit_item(request, id):
    id = decrypt_id(id)
    item = Item.objects.get(id=id)
    form = ItemForm(request.POST or None, request.FILES or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect('menu:index')
    
    return render(request, 'menu/item-form.html', {'form': form, 'item': item})

def delete_item(request, id):
    id = decrypt_id(id)
    item = Item.objects.get(id=id)

    if request.method=='POST':
        item.delete()
        return redirect('menu:index')
    return render(request, 'menu/item-delete.html', {'item': item})
    
