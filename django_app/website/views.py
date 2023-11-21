# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def home(request):
    # Check to see if loged in
    if request.method == 'POST': #after filling the form, whn you click submit, it will send a http request to the server, with the method in it.
        # to get the information tiped by the user:
        user_name = request.POST['user_name']
        password = request.POST['password']
        # to Authenticate:
        #in this case we used the user input as authentication, but instead of it, it should point to the informations saved in the database user_profile.
        auth = authenticate(request, user_name= user_name, password= password)
        if auth is not None:
            login(request, auth)
            messages.success(request, 'You are logged in!')
            return redirect('home')
        else:
            messages.success(request, 'Wrong user name or password, recheck it and try again.')
            return redirect('home')
    else:  
        return render(request, 'home.html', {})

#to have a eparated page to log in:
#def login_user(request):
#    pass
#if you do no want to oyu can add it in home aswell.

def logout_user(request):
    pass

