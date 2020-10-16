from django.shortcuts import render,redirect
from .forms import RegisterForm,LoginForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
# Create your views here.

def register(request):
    
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        new_user = User(username=username)
        new_user.set_password(password)
        new_user.save()
        login(request,new_user)
        #messages.add_message(request, messages.INFO, 'Başarıyla kayıt oldunuz', extra_tags='danger')
        messages.success(request,"Başarıyla kayıt oldunuz")
        return redirect("index")
    context={
        "form":form
    }
    return render(request,template_name="register.html",context=context)
        
def login_user(request):
    form = LoginForm(request.POST or None)
    context={
        "form":form
    }
    print(request.method)
    if form.is_valid() and request.method == "POST":
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username = username,password = password)
        if user is None:
            messages.add_message(request, messages.INFO, 'Kullanıcı adı veya parolası yalnış', extra_tags='danger')
            return render(request,"login.html",context)
        messages.success(request,"Başarıyla giriş yaptınız")
        login(request,user)
        return redirect("index")
    messages.add_message(request, messages.INFO, 'Kullanıcı adı veya parolası yalnış', extra_tags='danger')
    return render(request,"login.html",context)

def logout_user(request):
    logout(request)
    messages.success(request,"Çıkış Yaptınız")
    return redirect("index")