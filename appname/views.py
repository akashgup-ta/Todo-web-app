from django.shortcuts import render , redirect
from django.contrib import messages # import this
from django.contrib.auth.models import User # import this
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from .models import Mytodo
from .forms import TodoForm





# Create your views here.

def home(request):
    if not request.user.is_authenticated: #this is form signin
        return redirect("/sign_in/")
    tasks = Mytodo.objects.all()
    form = TodoForm()
    if request.method ==  'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()

    return render(request,'home.html', {'tasks':tasks,'form':form} )

def deleteItem(request, ak):
    task = Mytodo.objects.get(id=ak)
    task.delete()
    return redirect('home')

def updateItem(request, ak):
    todo = Mytodo.objects.get(id=ak)
    updateForm = TodoForm(instance=todo)
    if request.method == 'POST':
        updateForm = TodoForm(request.POST, instance= todo)
        if updateForm.is_valid():
            updateForm.save()
            return redirect('home')
    return render(request, 'updateItem.html', {'todo':todo, 'updateform':updateForm})





def sign_in(request):

    if request.user.is_authenticated:
        return redirect("/")
    if request.method=="POST":
        
        email=request.POST['email']
        userpassword=request.POST['password']
        user=authenticate(username=email,password=userpassword)

        if user is not None:
            login(request,user)
            messages.success(request,"Login Success")
            return redirect('/')

        else:
            messages.error(request,"Invalid email or password")
            return redirect('/sign_in/')
    return render(request,'sign_in.html')


def sign_up(request):

    if request.user.is_authenticated:
        return redirect("/")
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['pass1']
        confirm_password=request.POST['pass2']
        if password!=confirm_password:
            messages.warning(request,"Password is not matched... Try again")
            return render(request,'sign_up.html')
            
            
        try:
            if User.objects.get(email=email): 
                messages.warning(request,"Email is already Taken")
                return render(request,'sign_up.html')

        except Exception as identifier:
            pass

        
        user = User.objects.create_user(email,email,password)
        user.is_active=True
        user.save()
        
        return redirect('/sign_in/')

    return render(request,'sign_up.html')

def log_out(request):
    logout(request)
    return redirect('/sign_in/')

