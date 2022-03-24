from django.shortcuts import render, redirect
from .models import User

from .forms import UserForm


def index(request):

    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def successfully(request):
    return render(request, 'main/successfully.html')


def registration(request):
    return render(request, "main/registration.html")


def create(request):
    error = ''
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('successfully')
        else:
            error = "Invalid!"

    form = UserForm()
    context = {'form': form, 'error': error}
    return render(request, 'main/create.html', context)


def registration(request):
    return render(request, 'main/registration.html')


def login(request):
    return render(request, 'main/login.html')
