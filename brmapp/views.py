from django.shortcuts import render
from brmapp.forms import NewBookForm, SearchForm
from .import models
from django.http import HttpResponse, HttpResponseRedirect


def view_books(request):
    books = models.Book.objects.all()
    username=request.user.username
    return render(request, 'brm/view_books.html', {'books': books, })

def new_book(request):
    form = NewBookForm()
    return render(request, 'brm/new_book.html', {'form': form})


def add_book(request):

    if request.method == 'POST':
        form = NewBookForm(request.POST)
        book = models.Book()
        book.title=form.data['title']
        book.price=form.data['price']
        book.author=form.data['author']
        book.publisher=form.data['publisher']
        book.save()
        messages.success(request, 'Record Stored')
        s="record stored<br> <a href= '/brmapp/view-books'>View all books</a>" 
    

    return HttpResponse(s)


def edit_book(request):
    book = models.Book.objects.get(id=request.GET['bookid'])    
    fields = {'title':book.title, 'price':book.price, 'author':book.author,'publisher':book.publisher}
    form=NewBookForm(initial=fields)
    return render(request, 'brm/editbook.html', {'form':form, 'book':book})


def edit(request):
    if request.method =='POST':
        form = NewBookForm(request.POST)
        book.models.Book()
        book.id=request.POST['bookid']
        book.title=form.data['title']
        book.price=form.data['price']
        book.author=form.data['author']
        book.publisher=form.data['publisher']
        book.save()
    return HttpResponseRedirect('brmapp/view-books')


def delete_book(request):
    bookid=request.GET['bookid']
    book=models.Book.objects.filter(id=bookid)
    book.delete()
    return HttpResponseRedirect('brmapp/view-books')


def searchbook(request):
    form = SearchForm()
    return render(request, 'brm/search_book.html', {'form':form})

def search(request):
    form = SearchForm(request.POST)
    books=models.Book.objects.filter(title=form.data['title'])
    return render(request, 'brm/search_book.html', {'form':form, 'books':books})
