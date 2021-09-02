from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from account.forms import AccountForm
from logic.models import ExpertiseRequest, ExpertiseAnswer


# Create your views here.

def login_out(request):
    logout(request)
    return redirect("home")


def login_in(request):
    context = {}
    user = request.user

    if user.is_authenticated:
        return redirect("home")

    form = AccountForm()

    if request.POST:
        form = AccountForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                return redirect("home")
            else:
                context['error'] = "Невірний логін або пароль"

    context['login_form'] = form
    return render(request, 'login/login.html', context)


def my_page(request):
    context = {}
    user = request.user
    context['user'] = user
    return render(request, 'login/Personal_Page.html', context)


def expertise_requests(request):
    context = {}
    expertise_requests = ExpertiseRequest.objects.all()
    context['expertise_requests'] = expertise_requests
    return render(request, 'login/expertise_requests.html', context)