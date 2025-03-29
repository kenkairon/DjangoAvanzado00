from django.shortcuts import render
from categories.models import Category
# Create your views here.
def index(request):
    context ={
        'categories': Category.objects.all()
    }
    return render(request, 'categories/index.html')