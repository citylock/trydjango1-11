import random
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    num = None
    some_list = [ 
        random.randint(1, 100000), 
        random.randint(1, 100000), 
        random.randint(1, 100000)
    ]

    conditional_bool_item =  False

    if conditional_bool_item: 
        num = random.randint(1, 100000)

    context = {
        "num" : num, 
        "some_list" : some_list
    }
    return render(request, "home.html", context) 


def about(request):
    context = {
    }
    return render(request, "about.html", context) 


def contact(request):
    context = {
    }
    return render(request, "contact.html", context) 