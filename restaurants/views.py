from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView

from .models import RestaurantLocation
from .forms import RestaurantCreateForm, RestaurantLocationCreateForm


# Create your views here.
@login_required(login_url='/login/')
def restaurant_createview(request):
    form = RestaurantLocationCreateForm(request.POST or None)
    errors = None
    if form.is_valid():
        if request.user.is_authenticated():
            instance = form.save(commit=False)
            # customize
            # like a pre_save
            instance.owner = request.user
            instance.save()
            # like a post_save
            return HttpResponseRedirect('/restaurants/')
        else: 
            return HttpResponseRedirect('/login/')
    if form.errors: 
        errors = form.errors

    template_name = 'restaurants/form.html'
    context = { "form": form, 
                "errors": errors
            }
    return render(request, template_name, context)    


def restaurant_listview(request): 
    template_name = 'restaurants/restaurant_list.html'
    queryset = RestaurantLocation.objects.all()
    context = {
    #    "object_list" : [1,2,3,4,5]
        "object_list" : queryset
    }
    return render(request, template_name, context)

def restaurant_detailview(request, slug): 
    template_name = 'restaurants/restaurantlocation_detail.html'
    obj = RestaurantLocation.objects.get(slug=slug)
    context = {
        "object" : obj
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
    queryset = RestaurantLocation.objects.all() # filter(category__iexact='asian')

    # def get_context_data(self, *args, **kwargs):
    #     print(self.kwargs)
    #     context = super(RestaurantDetailView, self).get_context_data(*args, **kwargs)
    #     print (context)
    #     return context

    # def get_object(self, *args, **kwargs):
    #     rest_id = self.kwargs.get('rest_id')
    #     obj = get_object_or_404(RestaurantLocation, id=rest_id) # pk = rest_id 
    #     return obj
    # LoginRequiredMixin, 
class RestaurantLocationCreateView(LoginRequiredMixin, CreateView):
    form_class = RestaurantLocationCreateForm
    template_name = 'restaurants/form.html'
    success_url = '/restaurants/'
    # login_url = '/login/'    # also can set login_url in setting.py 

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user # NOT be anomyous users
        return super(RestaurantLocationCreateView, self).form_valid(form)


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

