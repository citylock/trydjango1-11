from django.shortcuts import render
from django.views.generic import ListView, UpdateView, CreateView, DetailView

from .models import Item
from .forms import ItemForm

# Create your views here.


class ItemListView(ListView):
    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)



class ItemDetailView(DetailView):
    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)



class ItemCreateView(CreateView):
    form_class = ItemForm
    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)



class ItemUpdateView(UpdateView):
    form_class = ItemForm
    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)
