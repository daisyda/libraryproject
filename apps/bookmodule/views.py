from django.shortcuts import render
from django.http import HttpResponse
from .models import Book


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

def links(request):
    """ Render the HTML5 links page """
    return render(request, "bookmodule/links.html")

def text_formatting(request):
    """ Render the text formatting page """
    return render(request, "bookmodule/text_formatting.html")

def listing(request):
    """ Render the listing page """
    return render(request, "bookmodule/listing.html")

def tables(request):
    """ Render the tables page """
    return render(request, "bookmodule/tables.html")

def search_books(request):
    if request.method == "POST":
        string = request.POST.get('keyword', '').lower()
        isTitle = request.POST.get('option1')
        isAuthor = request.POST.get('option2')

        # Get books
        books = __getBooksList()
        newBooks = []

        for item in books:
            contained = False
            if isTitle and string in item['title'].lower():
                contained = True
            if not contained and isAuthor and string in item['author'].lower():
                contained = True

            if contained:
                newBooks.append(item)

        return render(request, 'bookmodule/bookList.html', {'books': newBooks})  # ✅ Redirect to results page

    return render(request, 'bookmodule/search.html')


def __getBooksList():
    book1 = {'id': 12344321, 'title': 'Continuous Delivery', 'author': 'J. Humble and D. Farley'}
    book2 = {'id': 56788765, 'title': 'Reversing: Secrets of Reverse Engineering', 'author': 'E. Eilam'}
    book3 = {'id': 43211234, 'title': 'The Hundred-Page Machine Learning Book', 'author': 'Andriy Burkov'}
    return [book1, book2, book3]

def book_list(request):
    books = Book.objects.all()  # Retrieve all books from the database
    return render(request, 'bookmodule/bookList.html', {'books': books})

def simple_query(request):
    mybooks = Book.objects.filter(title__icontains='and')  # Filter books with "and" in the title
    return render(request, 'bookmodule/bookList.html', {'books': mybooks})


def complex_query(request):
    mybooks = Book.objects.filter(
        author__isnull=False  # Ensure author exists
    ).filter(
        title__icontains='and'  # Title contains "and"
    ).filter(
        edition__gte=2  # Edition is 2 or greater
    ).exclude(
        price__lte=100  # Exclude books with price ≤ 100
    )[:10]  # Limit results to 10

    if len(mybooks) >= 1:
        return render(request, 'bookmodule/bookList.html', {'books': mybooks})
    else:
        return render(request, 'bookmodule/index.html')