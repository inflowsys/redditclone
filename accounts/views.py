from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login , logout


# Create your views here.
def signup(request):

    if request.method == 'POST':

        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(username = request.POST['username'], password=request.POST['password1'])
            login(request,user)
            return redirect ('home')
        else:
            return render(request, 'accounts/signup.html', {'error':'password do not match'})



    else:
        return render(request, 'accounts/signup.html')




def loginview(request):

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']


        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            if 'next' in request.POST:
                return redirect (request.POST['next'])
            else:
                return redirect ('home')
        else:
            return render(request, 'accounts/login.html', {'error':'no such user, please try again'})

    else:
        return render(request, 'accounts/login.html')


def logoutview(request):
    logout(request)
    return redirect ('home')
