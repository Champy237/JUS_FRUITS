from django.shortcuts import render,get_object_or_404, redirect
from django.http import HttpResponse
from .models import *
from os import *
from .forms import InstriptionForm
from django.contrib import messages
# from .forms import someform
import os







'''def home(request):
    return HttpResponse("hello world")'''

#def contact(request,book_id):
    #context = {"book" : get_object_or_404(Task,pk = book_id)}
     #return render(request,'index.html',context)
    #def index(request):
    #return render(request,'index.html')


# def index(request):
#     if request.method == 'POST':
#         form = someform(request.POST)

#         if form.is_valid():
#             return redirect("index")
         
#     else:
#         form = someform()
#     context = {"form" : form}
#     return render(request,"index.html",context)





def home(request):
    fruit=jus.objects.all()[:3]
    return render(request,'pages/home.html',context={'fruits':fruit})


def apropo(request):
    fruit=jus.objects.all()
    print(fruit[0].name)
    print(fruit[0].ingredient)
    print(fruit[0].price)
    print(fruit[0].diabetic)
    return render(request,'pages/apropos.html',context={'fruits':fruit})

def about(request):
    fruit = jus.objects.all()
    print(fruit[0].name)
    print(fruit[0].ingredient)
    print(fruit[0].price)
    print(fruit[0].diabetic)
    return render(request, 'pages/about.html', context={'fruits':fruit})


def product(request):
    fruit = jus.objects.all()
    print(fruit[0].name)
    print(fruit[0].ingredient)
    print(fruit[0].price)
    print(fruit[0].diabetic)
    return render(request, 'pages/product.html', context={'fruits':fruit})


def detail(request, fruit_id):
    fruit = get_object_or_404(jus, pk=fruit_id)  # ✅ Utilisation correcte
    return render(request,'pages/detail.html', {"fruit": fruit})


def galerie(request):
    fruit = jus.objects.all()
    print(fruit[0].name)
    print(fruit[0].ingredient)
    print(fruit[0].price)
    print(fruit[0].diabetic)
    return render(request,'pages/galerie.html', context={'fruits':fruit})


def inscription(request):
    form = InstriptionForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'compte cree pour { username }.vous pouvez maintenant vous connecter.')
            return redirect('connexion')
        else:
            form = InstriptionForm()
    return render(request,'pages/inscription.html',{'form':form})

# else :
# 14
# form = InscriptionForm ()
# 15
# return render ( request , ’ blog / inscription . html ’ , { ’ form ’:
# form })
'''def home(request):
    contact_form = ContactForm()
    return render(request,'index.html',{'contact_form' : contact_form})


# Create your views here.'''
