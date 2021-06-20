from django.shortcuts import render,redirect
from django.contrib import messages 
from django.contrib.auth.models import User,auth

from . models import Post

# Create your views here.
def home(request):
    return render(request,'index.html')

def login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username, password = password)
        if user is not None:
            auth.login(request, user)  
            messages.info(request, 'Success: You are now logged in.') 
            return redirect('home')

        else:
            messages.info(request, 'User does not exist!!')
            return redirect('login')
   
    else:
        return render(request,'login.html')    


    
def post(request):
    if request.method == 'POST':
        text = request.POST['text']
        user = request.POST.get('user')
        post = Post.objects.create(user=user,text=text)
        post.save()
        messages.info(request, 'Post created ..')


    return render(request,'post.html')
    
      


def register(request):
    if request.method == 'POST':

        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email= request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username = username).exists():
                messages.info(request, 'username already taken..')
               
                return redirect('register')

            elif User.objects.filter(email = email).exists():
                messages.info(request, 'Email already taken ..')
                
                return redirect('register')

            else: 
                user = User.objects.create_user(first_name=firstname,last_name=lastname,username=username,email=email, password=password1)
                user.save()
                messages.info(request, 'User Created Successfully ..')
                print('user created')
                return redirect('login')

        else:
            messages.info(request, 'Password is not matching ..')
            print('password not matching')
            return redirect('register')
    
    else:
        return render(request,'register.html')



def logout(request):
    auth.logout(request)
    return redirect('home')         