from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm #Django Built in Form for creating users| not using it anymore because we inheret from it in our form
from django.contrib import messages #message.success message.debug
from django.shortcuts import redirect #*Important how to redirect
from .forms import UserRegistrationForm
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




