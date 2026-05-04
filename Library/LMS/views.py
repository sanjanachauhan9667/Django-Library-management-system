from django.shortcuts import render , redirect
from .models import LibraryHub
from django.http import HttpResponse
from django.contrib import messages


# Create your views here.

# Home---------------------------------------------------------------------- 
def home(request):
    return render(request,'LMS/home.html')

def add_book(request):
    message = ''
    
    if request.method == 'POST':
        name = request.POST.get('name')
        author = request.POST.get('author')
        
        if name and author:
            LibraryHub.objects.create(name=name, author=author, status= 'available')
            messages.success(request,'Record Added Successfully')
            return redirect('add')
            

        else: 
             message = 'Fill All Fields!'
    
    return render(request,'LMS/add.html',{'message':message})

# Search ------------------------------------------------------------------------
def search_book(request):

    books = []
    message = ''

    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'search':
            try:
                book_id = request.POST.get('id')
                books = LibraryHub.objects.filter(id = book_id)

                if books:
                    message = 'Book Found SuccessFully!'

                else:
                    message = 'Book Not Found!'

            except:
                message = 'Invalid Id!'

        elif action == 'search_all':
            books = LibraryHub.objects.all()
            message = 'List Of Books'


    return render(request,'LMS/search.html',{'books':books ,'message':message})

# Issue ---------------------------------------------------------------------------

def issue_book(request):

    if request.method == 'POST':
        book_id = request.POST.get('id')

        if not book_id:
            messages.error(request,'Please Enter Book Id!')
            return redirect('issue')
        
        try:
            book = LibraryHub.objects.get(id=book_id)

            if book.status == 'available':
                book.status = 'issued'
                book.save()
                messages.success(request,'BOOK ISSUED SUCCESSFULLY')

            else:
                messages.warning(request,'BOOK NOT AVAILABLE!')

        except:
            messages.error(request,'INVALID BOOK ID!')
        return redirect('issue')


    return render(request,'LMS/issue.html')


# Return ------------------------------------------------------------------------------

def return_book(request):

    if request.method == 'POST':
        book_id = request.POST.get('id')

        if  not book_id:
            messages.error(request,'Please Enter Book ID!')
            return redirect('return')
        
        try:
            book = LibraryHub.objects.get(id=book_id)

            if book.status == 'issued':
                book.status = 'available'
                book.save()
                messages.success(request,'BOOK RETURNED SUCCESSFULLY!')
            else:
                messages.warning(request,'BOOK IS NOT RETURNED!')

        except:
            messages.error(request,'INVALID BOOK ID')
        return redirect('return')
    
    return render(request,'LMS/return.html')

# Delete -------------------------------------------------------------------------------

def delete_book(request):
    books = []
    message = ''

    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'delete':
            try:
                book_id = request.POST.get('id')

                if not book_id:
                    message = 'Please Enter Book ID!'
                else:
                    book = LibraryHub.objects.get(id = book_id)
                    book.delete()
                    books = LibraryHub.objects.all() 
                    message = 'BOOK DELETED SUCCESSFULLY'

            except:
                message = 'INVALID BOOK ID!'

        elif action == 'delete_all':
            LibraryHub.objects.all().delete()
            books = []
            message = 'All BOOK DELETED SUCCESSFULLY!'

    return render(request,'LMS/delete.html',{'books':books,'message':message})

            









