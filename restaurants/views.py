from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView

from .models import RestaurantLocation

# Create your views here.
def restaurant_listview(request): 
    template_name = 'restaurants/restaurant_list.html'
    queryset = RestaurantLocation.objects.all()
    context = {
    #    "object_list" : [1,2,3,4,5]
        "object_list" : queryset
    }
    return render(request, template_name, context)


class RestaurantListView(ListView):
    # queryset = RestaurantLocation.objects.all()
    # template_name = 'restaurants/restaurant_list.html'
    # Default template_name restaurants/restaurantlocation_list.html


    def get_queryset(self): 
        print (self.kwargs)
        slug = self.kwargs.get('slug')
        if slug: 
            queryset = RestaurantLocation.objects.filter(
                Q(category__iexact=slug) | 
                Q(category__icontains=slug)
            )
        else: 
            queryset = RestaurantLocation.objects.all()
        return queryset

class RestaurantDetailView(DetailView):
    queryset = RestaurantLocation.objects.all()

    # def get_context_data(self, *args, **kwargs):
    #     print(self.kwargs)
    #     context = super(RestaurantDetailView, self).get_context_data(*args, **kwargs)
    #     print (context)
    #     return context

    def get_object(self, *args, **kwargs):
        rest_id = self.kwargs.get('rest_id')
        obj = get_object_or_404(RestaurantLocation, id=rest_id) # pk = rest_id 
        return obj


# class SearchRestaurantListView(ListView):
#     # queryset = RestaurantLocation.objects.filter(category__iexact='mexican')
#     template_name = 'restaurants/restaurant_list.html'

#     def get_queryset(self): 
#         print (self.kwargs)
#         slug = self.kwargs.get('slug')
#         if slug: 
#             queryset = RestaurantLocation.objects.filter(
#                 Q(category__iexact=slug) | 
#                 Q(category__icontains=slug)
#             )
#         else: 
#             queryset = RestaurantLocation.objects.filter.none()
#         return queryset

class MaxicanRestaurantListView(ListView):
    queryset = RestaurantLocation.objects.filter(category__iexact='mexican')
    template_name = 'restaurants/restaurant_list.html'

class AsianFusionRestaurantListView(ListView):
    queryset = RestaurantLocation.objects.filter(category__iexact='Asian Fusion')
    template_name = 'restaurants/restaurant_list.html'

