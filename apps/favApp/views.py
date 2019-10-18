from django.shortcuts import render, redirect
from apps.logRegApp.models import User
from apps.favApp.models import Book
from django.contrib import messages

# Create your views here.
def books(request): # on main page
    context = {
        "books": Book.objects.all(),
        "currentUser": User.objects.get(id=request.session['userid'])
    }
    return render(request, "favApp/books.html", context)

def addBook(request):
    errors = Book.objects.basic_validator(request.POST)
    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/books")
    else:
        uploadUser = User.objects.get(id = request.session['userid'])
        uploadTitle = request.POST['title']
        uploadDesc = request.POST['desc']
        newBook = Book.objects.create(uploadedBy = uploadUser, title=uploadTitle, desc=uploadDesc)
        newBook.usersWhoLike.add(uploadUser)
        return redirect(f"/books/{newBook.id}")

def specificBook(request, num): #on the specific book page books/<num>
    context = {
        "book": Book.objects.get(id=num),
        "currentUser": User.objects.get(id=request.session['userid'])
    }
    return render(request, "favApp/specificBook.html", context)

def addFavorite(request):
    currentUser = User.objects.get(id=request.session['userid'])
    currentBook = Book.objects.get(id=request.POST['bookID'])
    currentBook.usersWhoLike.add(currentUser)
    return redirect(f"books/{currentBook.id}")

def unfavorite(request):
    currentUser = User.objects.get(id=request.session['userid'])
    currentBook = Book.objects.get(id=request.POST['bookID'])
    currentBook.usersWhoLike.remove(currentUser)
    return redirect(f"books/{currentBook.id}")

def update(request):
    errors = Book.objects.basic_validator(request.POST)
    updateBook = Book.objects.get(id=request.POST['bookID'])
    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f"/books/{updateBook.id}")
    else:
        updateBook = Book.objects.get(id=request.POST['bookID'])
        try:
            update = request.POST['update']
            updateBook.title=request.POST['title']
            updateBook.desc=request.POST['desc']
            updateBook.save()
            return redirect(f"/books/{updateBook.id}")
        except:
            delete = request.POST['delete']
            updateBook: Book.objects.get(id=request.session['bookID'])
            updateBook.delete()
            return redirect("/books")
    


