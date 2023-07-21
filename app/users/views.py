from django.shortcuts import render, redirect
from users.forms import LogInForm, SignUpForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def user_login(request):
    if request.method == "POST":
        form = LogInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("home")
    else:
        form = LogInForm()
    context = {
        "form": form,
    }
    return render(request, "login.html", context)


def user_logout(request):
    logout(request)
    return redirect("login")


def user_signup(request):
    form = SignUpForm(request.POST)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        first_name = form.cleaned_data.get("first_name")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        confirm = form.cleaned_data.get("password_confirm")
        if password == confirm:
            user = User.objects.create_user(username, email, first_name,
                                            password=password)
            login(request, user)
            return redirect("home")
        else:
            form.add_error("password", "Passwords do not match")
    else:
        form = SignUpForm()
    context = {
        "form": form,
    }
    return render(request, "signup.html", context)
