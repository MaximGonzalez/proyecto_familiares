from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Yo, Familiar

# Create your views here.
def yo(request):
    yo = Yo.objects.all()
    return render(request, 'yo.html', {'yo' : yo})

def familiares(request):
    return render(request, 'familiares.html')