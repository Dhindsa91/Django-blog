from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm #Django Built in Form for creating users| not using it anymore because we inheret from it in our form
from django.contrib import messages #message.success message.debug
from django.shortcuts import redirect #*Important how to redirect
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm
# Create your views here.


#Using a form from django to do registration
#the form info is being posted back here
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST) #Loads all the data from the form into the var
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account Created for {username}')                          #hows this going to navbar in base.html?
            return redirect('login') #blog is the url pattern name for the blog home          #This is also passing the data
    else:
        form = UserRegistrationForm #our created form
    


    return render(request, 'users/register.html', {'form': form})
    
    #You can also use request.POST['username']


# def login(request): #This doesnt need to be created because this is a pre-existing view already in Django

@login_required    #this hold the redirect page address when you log in it takes you to where you wanted to go
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            username = u_form.cleaned_data.get('username')
            messages.success(request, f'Account Updated for {username}')
            return redirect('profile')  
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)                                 #^ update being saved?

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request,'users/profile.html', context)




