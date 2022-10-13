from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.




def register(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']
        
        email_already_exist = User.objects.filter(email=email).exists()
        
        if email_already_exist:
            messages.info(request,'Email already exists')
            return redirect('register')
        elif len(password) < 4 :
            messages.info(request,'password too short')
        else:
            user = User.objects.create_user(email=email,first_name=fname,last_name=lname, username=lname,password=password)
            user.save()
            print('user created successfully')
            return redirect('login')
            
    return render(request,'register.html')





def login(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            messages.warning(request,'Credentials does not match')
            print('something went wrong')
            return redirect('login') 
        
    
    return render(request,'login.html')


