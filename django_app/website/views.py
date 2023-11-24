# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUp, UserProfileForm, KitchenForm 
from .models import UserProfile, Kitchen

def home(request):
    #to take all the data from your table:
    kitchen_appliances = Kitchen.objects.all().order_by('created_at')
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
        #passin data that you took from the data base to be available in the home page:
        return render(request, 'home.html', {'kitchen_appliances': kitchen_appliances})

def appliances(request):
    kitchen_appliances = Kitchen.objects.all().order_by('created_at')
    return render(request, 'appliances.html', {'kitchen_appliances': kitchen_appliances})

def delete_kichen_appliance(request, pk):
    delete_it = Kitchen.objects.get(id=pk)
    delete_it.delete()
    messages.success(request, 'Deleted Successfully!')
    return redirect('appliances')

def add_kitchen_record(request):
    form = KitchenForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                messages.success(request, 'Added Successfully!')
                return redirect('appliances')
        return render(request, 'add_kitchen_record.html', {'form':form})

def logout_user(request):
    logout(request)
    messages.success(request, 'You are logged out.')
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUp(request.POST)
        if form.is_valid():
            form.save()
			# clean the form fields: Create a new instance of the model and populate it with the cleaned data, including the additional fields from the form.
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            # Authenticate and login
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You Have Successfully Registered! Welcome!")
            return redirect('profile') # 
        else:
            # If the form is not valid, display form errors
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")

    context = {'form':SignUp()}
    return render(request, 'register.html', context)
    #or #form = SignUp()
        #return render(request, 'register.html', {'form':form})
    
def profile(request):
    try:
        user_profile = request.user.userprofile
    except UserProfile.DoesNotExist:
        user_profile = None

    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST, instance=user_profile)
        if profile_form.is_valid():
            profile = profile_form.save(commit=False)
            profile.user = request.user
            profile.save()
    else:
        profile_form = UserProfileForm(instance=user_profile)

    return render(request, 'profile.html', {'profile_form': profile_form})