from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth  import authenticate,  login, logout
from django.contrib import messages
from django.db.models import Q
# Create your views here.
def home(request):
    if request.user.is_authenticated:
        usr = User.objects.all().filter(~Q(username=request.user))
        dic={'usr':usr}
        
        return render(request,'home/index.html',dic)
    else:
        return render(request,'home.html')

def handleSignUp(request):
    if request.method=="POST":
        # Get the post parameters
        username=request.POST['username']
        email=request.POST['email']
        pass1=request.POST['password']
        fname=request.POST['fname']
        lname=request.POST['lname']
        try:
            user= User.objects.get(username=username)

            messages.error(request, "Username already exists")
            return redirect('home')
        except User.DoesNotExist:
            try:
                user= User.objects.get(email=email)

                messages.error(request, "email already exists")
                return redirect('home')
            except User.DoesNotExist:
                myuser = User.objects.create_user(username, email, pass1)

        myuser.first_name= fname
        myuser.last_name= lname
        myuser.save()
        return redirect('/')

    else:
        return HttpResponse("404 - Not found")

def handeLogin(request):
    if request.method=="POST":
        # Get the post parameters
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']

        user=authenticate(username= loginusername, password= loginpassword)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("/")

    return HttpResponse("404- Not found")


def handelLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('home')
def loginPage(request):
    return render(request, 'login.html') 

def profile(request):
    return render(request,'home/myprofile.html')       