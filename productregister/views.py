from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'base.html')

def list_products(request):
        return render(request, 'products.html')

def alter_products(request):
        return render(request, 'products-form.html', data={})

def create_product(request):
        return render(request, 'products-form.html')

def list_categories(request):
        return render(request, 'categories.html')

def alter_categories(request):
        return render(request, 'categories-form.html', data={})

def create_category(request):
        return render(request, 'categories-form.html')