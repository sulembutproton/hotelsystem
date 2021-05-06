from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from .models import Chambre,Catalogue,Testimonial
# Create your views here.

def index (request):
    chambres= Chambre.objects.all()
    catalogues= Catalogue.objects.all()
    testimonials = Testimonial.objects.all()
    render(request,'index.html',{'testimonial': testimonials})
    render (request,'index.html',{'catalogues': catalogues})
    return render(request,"index.html",{'chambres': chambres})

@csrf_protect
def reservation (request):
    context = {}
    return render(request, "reservation.html", context)

def contact(request):
    return  render (request, "contact.html")

def blog (request):
    chambres = Chambre.objects.all()
    return render (request, "blog.html",{'chambres': chambres})

def about(request):
    return render (request, 'about.html')

