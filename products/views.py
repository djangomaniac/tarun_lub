from django.shortcuts import render, redirect
from .models import *


def product_catalogue(request):
    sulfonates = Sulfonate.objects.all()
    indlubs = IndustrialLubricant.objects.all()
    texlubs = Textile.objects.all()
    autolubs = AutomotiveLubricant.objects.all()

    context = {
        'sulfonates': sulfonates,
        'indlubs': indlubs,
        'texlubs': texlubs,
        'autolubs': autolubs,
    }
    return render(request, 'products_catalogue.html', context)


def sulfo_view(request):
    products = Sulfonate.objects.all()
    context = {
        'products': products,
        'name': 'Sulfonates',
    }
    return render(request, 'category_page.html', context)


def indus_view(request):
    products = IndustrialLubricant.objects.all()
    context = {
        'products': products,
        'name': 'Industrial Lubricants',
    }
    return render(request, 'category_page.html', context)


def tex_view(request):
    products = Textile.objects.all()
    context = {
        'products': products,
        'name': 'Textile',
    }
    return render(request, 'category_page.html', context)


def auto_view(request):
    products = AutomotiveLubricant.objects.all()
    context = {
        'products': products,
        'name': 'Automotive Lubricants',
    }
    return render(request, 'category_page.html', context)
