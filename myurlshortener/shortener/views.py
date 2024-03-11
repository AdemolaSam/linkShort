from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .forms import Urlform, Register, Login
from django.contrib import messages
from .models import User, Url
from .util import generate_random_chars
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail



def index(request):
    return render(request, "shortener/index.html")

def register(request):
    if request.method == "POST":
        form = Register(request.POST)
        if form.is_valid():
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            confirm_pasword = request.POST['confirm_password']

            if password != confirm_pasword:
                messages.error(request, "Passwords does not match. Try again")
                return render(request, "shortener/register.html", {"form":form})

            User.objects.create_user(username=username, email=email, password=password)
            return redirect("login")
        
    else:
        form = Register()
    return render(request, "shortener/register.html", {"form":form})


def login_view(request):
    if request.method == 'POST':
        form = Login(request.POST)
        if form.is_valid(): 
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            print(user)
            if user is not None:
                login(request, user)
                return redirect('get_url')
            
            messages.error(request, "Invalid username or password")
            return render(request, "shortener/login.html", {"form": form})
    else:
        form = Login()
    return render(request, 'shortener/login.html', {"form": form})

def logout_view(request):
    logout(request)
    return redirect("index")

@login_required
def get_url(request):
    if request.method == "POST":
        form = Urlform(request.POST)
        if form.is_valid():
            long_url = request.POST['url']
            short = generate_random_chars()

            try:
                Url.objects.create(link=long_url, shortened_link=short, owner=request.user)
                form = Urlform()
                return render(request, "shortener/short.html",{"result": short, "form":form})
            except Exception as e:
                return render(request, "shortener/error.html", {"error": e})
    else:
        form = Urlform()
    return render(request, "shortener/short.html", {"form": form})


def goto_link(request, url):
    try:
        link_obj = Url.objects.filter(shortened_link=url).first()  # Assuming 'link' is the field name in the Url model
        if link_obj:
            link_obj.clicks += 1
            return redirect(link_obj.link)
        else:
            return render(request, "shortener/error.html", {"error": "URL not found"})
    except Exception as e:
        print(e)
        return render(request, "shortener/error.html", {"error": e})
    
@login_required    
def my_urls(request, id):
    pass

    
def your_view(request):
    # Your view logic...
    
    # Send email
    subject = 'Subject of the email'
    message = 'Test message from Django'
    from_email = 'katashisasaki318@gmail.com'
    recipient_list = ['oduntanade2721@gmail.com']

    try:
        send_mail(subject, message, from_email, recipient_list)
        print("Email sent to: ", subject)
        return HttpResponse("Email sent!")
    except Exception as e:
        print(e)
        return render(request, "shortener/error.html", {"error":e})    