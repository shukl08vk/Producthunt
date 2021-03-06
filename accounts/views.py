from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth

def signup(request):
    if request.method=='POST':
        #user has info and want a account now
        #if request.POST['Username']=='' or request.POST['Username'] is None:
        #  return render(request, 'accounts/signup.html', {'error':'Username must not be Empty'})

        if request.POST['Password1']==request.POST['Password2']:
            try:
                user=User.objects.get(username=request.POST['Username'])
                return render(request, 'accounts/signup.html', {'error':'Username has already been taken'})
        
            except User.DoesNotExist:
                user=User.objects.create_user(request.POST['Username'],password=request.POST['Password1'])
                auth.login(request,user)
                return redirect('home')
        else:
             return render(request, 'accounts/signup.html', {'error':'password must match'})

    else:
        #user wants to enter info
        return render(request, 'accounts/signup.html')

def login(request):
    if request.method == 'POST':
        user=auth.authenticate(username=request.POST['Username'],password=request.POST['Password'])
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            return render(request,'accounts/login.html',{'error':'username or password is incorrect.'})

    else:   
        return render(request,'accounts/login.html')

def logout(request):
    #TODO need to do route to homepage
    # dont forget to logout
    if request.method=="POST":
        auth.logout(request)
        return redirect('home')


    render(request, 'accounts/signup.html')

