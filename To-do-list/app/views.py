from django.shortcuts import redirect, render
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Tasks

# Create your views here.
def home(request):
    return render(request, 'index.html')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user =  auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('account')
        else:
            messages.info(request, 'Username or Password is incorrect')
    return render(request, 'login.html')

def register(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        if User.objects.filter(email=email).exists():
            messages.info(request, "Email Address already exists")
        elif User.objects.filter(username=username).exists():
            messages.info(request, "Username already taken")
        else:
            user = User.objects.create_user(email=email, password=password, first_name=firstname, last_name=lastname, username=username)
            user.save()
            messages.info(request, "Account successfully created")

    return render(request, 'register.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def account(request):
    return render(request, 'account.html')

def logout(request):
    auth.logout(request)
    return redirect('home')

def add_task(request):
    if request.method == "POST":
        title = request.POST['title']
        description = request.POST['description']
        date = request.POST['date']
        category = request.POST['category']
        user = request.user
        new_tasks = Tasks.objects.create(title=title, content=description, date=date, category=category, user=user)
        return redirect("tasks")
    return render(request, 'addtask.html')


def tasks(request):
    tasks = Tasks.objects.filter(user=request.user).all()[:10]
    return render(request, 'tasks.html', {"tasks": tasks})


def task(request, id):
    task = Tasks.objects.get(id=id)
    return render(request, 'task.html', {"task":task})