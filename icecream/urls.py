from django.urls import path
from . import views
urlpatterns = [    
# path('admin', admin.site.urls),
path('',views.index,name='index'),
path('index.html',views.index,name='index'),
path('about.html',views.about,name='about'),
path('product.html',views.product,name='product'),
path('service.html',views.service,name='service'),
path('contact.html',views.contact,name='contact'),
path('gallery.html',views.gallery,name='gallery'),
]