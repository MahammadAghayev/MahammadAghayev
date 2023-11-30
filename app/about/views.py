from django.shortcuts import render
from .models import About
# Create your views here.

def about(request):  # function based
    about = About.objects.first()
    context = {
        'about' : about
    }
    return render(request, 'about/index.html', context)