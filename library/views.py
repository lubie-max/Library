from django.shortcuts import redirect, render
from .models import Book
from django.contrib.auth import login , logout , authenticate
from django.contrib.auth.models import User
from django.contrib import messages



def home(request ):
    books= Book.objects.all()
    if not request.user.is_authenticated:
        messages.error(request, 'Login for operating Library. ')

    context= {
        'books' : books ,
    }
    return render(request , 'index.html' , context)

def update_book(request, id):
    book = Book.objects.get(id=id) 
    print(book, '<<<<<<<')

    if request.method =="POST":
        book.title = request.POST['title']
        book.description = request.POST['description']
        book.cover = request.FILES['cover']

        # book = book(title=title , description=description , cover=cover)
        book.save()
        messages.success(request, 'Book has been updated successfully.')
        return redirect('/')
    context= {
        'book': book,
    }
    return render(request , 'update.html' , context)

def create_book(request):
    if request.method == "POST":
        title = request.POST['title']
        description = request.POST['description']
        cover = request.FILES['cover']

        book= Book.objects.create(title=title, description=description, cover=cover)
        book.save()
        messages.success(request, 'Book has been added successfully.')
  
    return render(request , 'create.html' )


def delete_book(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    messages.error(request, f" '{ book.title }' has been deleted.")

    return redirect('/')


def user_authentication(email , password):
    try:
        user= User.objects.get(email=email)

    except User.DoesNotExist:
        return None

    else :
        if user.check_password(password):
            return user

    return None 


def login_user(request):
 
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        
        user = user_authentication(email , password)
        
       
        if user is not None:
            login(request , user)
            print(request.user)
            messages.success(request, 'You have logged in.')

            return redirect('/')

        else :  
            messages.error(request, 'Wrong Password or Email.')
            return redirect('/login')
    

 
    return render(request , 'login.html')
    


def logout_user(request):
    try:
        logout(request)
        messages.info(request, 'You have logged out.')

        return redirect('/')

    except Exception as e:
        print(e)

    