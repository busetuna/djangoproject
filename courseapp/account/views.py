from email import message
from urllib import request
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout , update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm , PasswordChangeForm
from .forms import LoginUserForm, NewUserForm


def user_login(request):
    if request.user.is_authenticated and "next" in request.GET:
        return render(request, "account/login.html", {"error": "Yetkiniz yok."})

   
    if request.method == "POST":
        form = LoginUserForm(request, data=request.POST) 
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.add_message(request, messages.SUCCESS , "Giriş başarılı")
                nextUrl = request.GET.get("next", None)
                if nextUrl is None:
                    return redirect("index")
                else:
                    return redirect(nextUrl)
            else:
                return render(request, "account/login.html", {"form": form }) 
        else:
            return render(request, "account/login.html", {"form": form })
    else:
        form = LoginUserForm()
        return render(request, "account/login.html", {"form": form})
    
def user_register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        
        if form.is_valid():
            form.save()
            
            # Kullanıcı tarafından girilen ham şifreyi form'dan alalım
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect("index")
        else:
            return render(request, "account/register.html", {"form": form})
    else:
        form = NewUserForm()
        return render(request, "account/register.html", {"form": form})
    
def change_password(request):
    if request.method == "POST":
        form  = PasswordChangeForm(request.user, request.POST)
        if form.is_valid:
            user = form.save()
            update_session_auth_hash(request, user)
            message.success(request, "Parola güncellendi.")
            return redirect("change_password")
        else:
            return render(request, "account/change-password.html" , {"form": form})

    form = PasswordChangeForm(request.user)
    return render(request, "account/change-password.html" , {"form": form})




def user_logout(request):
    logout(request)
    return redirect("index")

