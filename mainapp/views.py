from django.shortcuts import render
from .models import USER

# Create your views here.

def main(request):
    return render(request, 'mainapp/main.html')
