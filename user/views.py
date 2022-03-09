from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages,auth
from .models import product

def home(request):        
    products =product.objects.all()
    return render(request, 'home.html',{'products':products})

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,
        password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            messages.info(request,
            'invalid username and password')
            return redirect('login')
    
    else:
        return render(request,'user/login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')


def add_user(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        password=request.POST['password1']
        password2=request.POST['password2']
        email=request.POST['email']

        if password==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username is taken')
                return redirect('add_user')

            elif User.objects.filter(email=email).exists():
                messages.info(request,'username is taken')
                return redirect('add_user')

            else:
                user=User.objects.create_user(username=username,
                password=password,
                email=email,first_name=first_name,
                last_name=last_name)
                user.save();
                return redirect('login')
        else:
            messages.info(request,'password is no matching..')
            return redirect('add_user')
    else:
        return render(request,'user/add_user.html')


def poster(request,pk):
    poster1=product.objects.get(id=pk)
    context={'posters':poster1}
    return render(request,'user/poster.html',context)


