from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    """ Render the home page (index.html) """
    name = request.GET.get("name") or "world!"
    return render(request, "bookmodule/index.html", {"name": name})

def list_books(request):
    """ Render the list of books page (list_books.html) """
    return render(request, "bookmodule/list_books.html")

def aboutus(request):
    """ Render the about us page (aboutus.html) """
    return render(request, "bookmodule/aboutus.html")

def viewbook(request, bookId):
    """ Render the details of a specific book """

    # Define available books (This should come from a database in the future)
    books = {
        123: {'id': 123, 'title': 'Continuous Delivery', 'author': 'J. Humble and D. Farley'},
        456: {'id': 456, 'title': 'Secrets of Reverse Engineering', 'author': 'E. Eilam'}
    }

    # Get the book details or set to None if not found
    targetBook = books.get(bookId, None)

    # Render book details page
    return render(request, "bookmodule/one_book.html", {"book": targetBook})

def index2(request, val1=0):
    """ Simple test function for handling URL parameters """
    return HttpResponse("value1 = " + str(val1))
