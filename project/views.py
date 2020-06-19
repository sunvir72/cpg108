from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import  User,auth

# Create your views here.

def home(request):
    return render(request,'home.html')
def user(request):
    return render(request,'userhtml.html')


def signup(request):
    if request.method == 'POST':
        print("hcbjhebryucqeucbugerv")
        form=UserCreationForm(request.POST)
        if(form.is_valid()):
            user=form.save()
        return redirect('ProjectHome')
    else:
        form=UserCreationForm()
        dict={'form':form}
        return render(request,'signup.html',dict)

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('user')
        else:
            return render(request, 'login')

    else:
        return render(request,'login.html')
