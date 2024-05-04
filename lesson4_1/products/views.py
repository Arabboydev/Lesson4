from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Category, ProductsAbout


def get_info(request):
    categories = Category.objects.all()
    context = {
        'categories':categories
    }
    return render(request, 'index.html',context=context)


def get_products_about(request, pk):
    products = ProductsAbout.objects.filter(category=pk)
    context = {
        'products': products
    }
    return render(request, 'products.html', context=context)


def detail(request, pk):
    product = ProductsAbout.objects.get(pk=pk)
    context = {
        'product': product
    }
    return render(request, 'detail.html', context=context)


def add_products(request):
    form = ProductForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('products:get_info')
    context = {
        'form': form
    }
    return render(request, 'create.html', context=context)


def update_products(request, pk):
    data = ProductsAbout.objects.get(pk=pk)
    form = ProductForm(request.POST, request.FILES,instance=data)
    if form.is_valid():
        form.save()
        return render('products:get_info')
    context = {
        'form':form
    }
    return render(request, 'update.html',context=context)