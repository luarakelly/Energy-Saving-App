# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUp

def home(request):
    # Check to see if loged in
    if request.method == 'POST': #after filling the form, whn you click submit, it will send a http request to the server, with the method in it.
        # to get the information tiped by the user:
        username = request.POST['username']
        password = request.POST['password']
        # to Authenticate:
        #in this case we used the user input as authentication, but instead of it, it should point to the informations saved in the database user_profile.
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You are logged in!')
            return redirect('home')
        else:
            messages.success(request, 'Wrong user name or password. Please try again.')
            return redirect('home')
    else:  
        return render(request, 'home.html', {})

#to have a separated page to login:
#def login_user(request):
#    pass
#if you do no want to oyu can add it in home aswell.

def logout_user(request):
    logout(request)
    messages.success(request, 'You are logged out.')
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUp(request.POST)
        if form.is_valid():
            form.save()
			# clean the form fields
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            # Authenticate and login
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You Have Successfully Registered! Welcome!")
            return redirect('home')
        else:
            # If the form is not valid, display form errors
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")

    context = {'form':SignUp()}
    return render(request, 'register.html', context)
    #or #form = SignUp()
        #return render(request, 'register.html', {'form':form})