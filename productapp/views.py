from django.shortcuts import render
from django.contrib import messages 
# Create your views here.
from . models import Product

# Create your views here.
def addproduct(request):
    if request.method == 'POST':

        name = request.POST['name']
        weight= request.POST['weight']
        price = request.POST['price']
        product = Product.objects.create(name=name,weight=weight,price=price)
        product.save()
        messages.info(request, 'Product created ..')

    return render(request,'addproduct.html')