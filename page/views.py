from django.shortcuts import render
from .models import Page
import random

def home(request):
    return render(request, 'home.html')

def count(request):
    full_text = request.GET['fulltext']
    name_list = full_text.split()
    count = request.GET['count']
    out = random.sample(name_list, int(count))
    return render(request, 'count.html', {'fulltext': full_text, 'count':count, 'out':out})
