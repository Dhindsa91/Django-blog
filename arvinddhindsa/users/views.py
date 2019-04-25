from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm #Django Built in Form for creating users
from django.contrib import messages #message.success message.debug
from django.shortcuts import redirect #*Important how to redirect
# Create your views here.


#Using a form from django to do registration

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST) #Loads all the data from the form into the var
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account Created for {username}')                          #hows this going to navbar in base.html?
            return redirect('blog-home') #blog is the url pattern name for the blog home          #This is also passing the data
    else:
        form = UserCreationForm()
    


    return render(request, 'users/register.html', {'form': form})
    