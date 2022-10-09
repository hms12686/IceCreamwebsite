from django.shortcuts import render
from django.http import HttpResponse

from icecream.models import ProductCategory

# Create your views here.
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def product(request):
    pc1 = ProductCategory()
    pc1.product_name = 'IceCream in Cone'
    pc1.product_price = 70
    pc2 = ProductCategory()
    pc2.product_name = 'IceCream in Cup'
    pc2.product_price = 150
    pc3 = ProductCategory()
    pc3.product_name = 'IceCream in Jar'
    pc3.product_price = 100
    pc4 = ProductCategory()
    pc4.product_name = 'IceCream for Family'
    pc4.product_price = 250
    return render(request,'product.html', {'pc1': pc1, 'pc2':pc2, 'pc3':pc3,'pc4':pc4})
def service(request):
    return render(request,'service.html')
def contact(request):
    return render(request,'contact.html')
def gallery(request):
    return render(request,'gallery.html')

