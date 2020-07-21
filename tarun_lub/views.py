from django.shortcuts import render, redirect
from enquiry.models import *


def home_page(request):
    visitors = Visitor.objects.all()[0]
    visitors.visit += 1
    visitors.save()
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        address = request.POST.get('address', '')
        message = request.POST.get('message', '')
        enquiry = Enquiry(name=name, email=email, phone=phone, address=address, message=message)
        enquiry.save()
    context = {'visitors': visitors, }
    return render(request, 'index.html', context)