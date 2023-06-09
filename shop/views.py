from django.shortcuts import render
from .models import Product , Contact
from math import ceil

# Create your views here.
from django.http import HttpResponse

def index(request):
    products = Product.objects.all()
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds':allProds}
    return render(request, 'shop/index.html', params)

def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    if(request.method == 'POST'):
        print(request)
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        phone = request.POST.get('phone','')
        desc = request.POST.get('msg','')
        
        contact = Contact(name = 'name' , email = 'email' , phone = 'phone' , Message = 'desc')
        contact.save()
    return render(request, 'shop/contact.html')

def tracker(request):
    return render(request, 'shop/tracker.html')

def search(request):
    return HttpResponse("We are at search")

def products(request , myid):
    # fetching products from data base
    product = Product.objects.filter(id=myid)
    print(product)

    return render(request, 'shop/productView.html' , {'product':product})

def checkout(request):
    return render(request, 'shop/checkout.html')
