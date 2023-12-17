from django.shortcuts import render, redirect
from .models import Receipe
from django.contrib import messages 
from django.contrib.auth.models import User
#from django.contrib.auth import authenticate, login, logout
#from django.contrib.auth.decorators import login_required

# Create your views here.
#@login_required(login_url="/login")
def index(request):
    if request.method == "POST":
          
        data  = request.POST 
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')
        receipe_image = request.FILES.get('receipe_image')
        
        Receipe.objects.create(
            receipe_name = receipe_name,
            receipe_description = receipe_description,
            receipe_image = receipe_image
        )
                    
        messages.success(request, "Your message is sent susseccfully")
        return redirect('/')
    queryset = Receipe.objects.all()
    
    
    if request.GET.get('search'):
        queryset = queryset.filter(receipe_name__icontains =  request.GET.get('search'))
        
    context = {'receipes':queryset}            
    return render(request, 'index.html', context)


#@login_required(login_url="/login")
def delete(request, id):
    queryset = Receipe.objects.get(id = id)
    queryset.delete()
    messages.warning(request, "Your message is  deleted!!")
     
    return redirect('/')


#@login_required(login_url="/login")
def update(request, id):
    
     queryset = Receipe.objects.get(id = id)
     
     if request.method =="POST":
         data  = request.POST 
         receipe_name = data.get('receipe_name')
         receipe_description = data.get('receipe_description')
         receipe_image = request.FILES.get('receipe_image')
         
         queryset.receipe_name = receipe_name
         queryset.receipe_description = receipe_description
          
         if receipe_image:
              queryset.receipe_image = receipe_image
              
         queryset.save()  
         return redirect("/") 
         
     context = {'receipe': queryset}
     
     
     return render(request,'update.html', context)
 
 

'''def register(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = User.objects.filter(username = username)
        
        if user.exists():
            messages.warning(request, "username is already taken.")
            return redirect('/register')
        
        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = username
        )
        
        
        user.set_password('passord')
        user.save()
        messages.success(request, "You Susseccfully Registered")
        return redirect('/register')       
    
    return render(request, 'register.html')
     
     
def login_user(request):
    
     if request.method == "POST":
         username = request.POST.get('username')
         password = request.POST.get('password')
        
         user = authenticate(request, username = username, password = password)

         if user is not None:
            login(request, user)
            return  redirect("/")
         else:
            return redirect( '/login')
            
     return render(request, 'login.html')


#@login_required(login_url="/login")
def logout_user(request):
    logout(request)
    return redirect('/login')'''
