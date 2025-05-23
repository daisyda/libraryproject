from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from django.db.models import Q
from django.db.models.functions import Lower
from django.db.models import Count, Sum, Avg, Max, Min
from django.db.models import Count
from apps.bookmodule.models import Address
from .models import Department
from .models import Department, Student
from django.db.models import Max
from .models import Course
from django.db.models import Min
from django.shortcuts import redirect
from .forms import GalleryItemForm
from .models import Student2, Address2
from .forms import Student2Form
from django.contrib.auth.decorators import login_required









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

def search(request):
    if request.method == "POST":
        string = request.POST.get('keyword').lower()
        isTitle = request.POST.get('option1')
        isAuthor = request.POST.get('option2')

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

        return render(request, 'bookmodule/bookList.html', {'books': newBooks})

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
        author__isnull=False
    ).filter(
        title__icontains='and'
    ).filter(
        edition__gte=2
    ).exclude(
        price__lte=100
    )[:10]  # نعرض فقط أول 10 نتائج

    if len(mybooks) >= 1:
        return render(request, 'bookmodule/bookList.html', {'books': mybooks})
    else:
        return render(request, 'bookmodule/index.html')


  
#lab 8: 


def lab8_task1(request):
    from .models import Book
    books = Book.objects.filter(Q(price__lte=80))
    return render(request, 'bookmodule/lab8_task1.html', {'books': books})



def lab8_task2(request):
    from .models import Book
    books = Book.objects.filter(
        Q(edition__gt=3) & (Q(title__icontains='co') | Q(author__icontains='co'))
    )
    return render(request, 'bookmodule/lab8_task2.html', {'books': books})



def lab8_task3(request):
    from .models import Book
    books = Book.objects.filter(
        ~Q(edition__gt=3) & ~Q(title__icontains='co') & ~Q(author__icontains='co')
    )
    return render(request, 'bookmodule/lab8_task3.html', {'books': books})


def lab8_task4(request):
    from .models import Book
    books = Book.objects.all().order_by(Lower('title'))
    return render(request, 'bookmodule/lab8_task4.html', {'books': books})

def lab8_task5(request):
    from .models import Book

    stats = Book.objects.aggregate(
        total_books=Count('id'),
        total_price=Sum('price'),
        average_price=Avg('price'),
        max_price=Max('price'),
        min_price=Min('price'),
    )

    return render(request, 'bookmodule/lab8_task5.html', {'stats': stats})

def students_per_city(request):
    city_stats = Address.objects.annotate(student_count=Count('student'))
    return render(request, 'bookmodule/lab8_task7.html', {'city_stats': city_stats})

# Lab 9:

def lab9_task1(request):
    departments = Department.objects.annotate(student_count=Count('student'))
    return render(request, 'bookmodule/lab9_task1.html', {'departments': departments})

def lab9_task2(request):
    courses = Course.objects.prefetch_related('students').all()
    return render(request, 'bookmodule/lab9_task2.html', {'courses': courses})




def lab9_task3(request):
    # نحسب أقل ID في كل قسم
    departments = Department.objects.annotate(first_student_id=Min('student__id'))

    result = []

    for dept in departments:
        if dept.first_student_id:
            student = Student.objects.get(id=dept.first_student_id)
            result.append({
                'department': dept.name,
                'student_name': student.name,
                'student_id': student.id,
                'student_age': student.age,
            })

    return render(request, 'bookmodule/lab9_task3.html', {'result': result})


    

def lab9_task4(request):
    departments = (
        Department.objects
        .annotate(student_count=Count('student'))
        .filter(student_count__gt=2)
        .order_by('-student_count')
    )
    return render(request, 'bookmodule/lab9_task4.html', {'departments': departments})

#lab 10:
from django.shortcuts import get_object_or_404

from .models import Book
from django.http import HttpResponse

def lab9_part1_listbooks(request):
    books = Book.objects.all()
    return render(request, 'bookmodule/lab9_part1_listbooks.html', {'books': books})



def lab9_part1_addbook(request):
    if request.method == "POST":
        title = request.POST.get('title')
        author = request.POST.get('author')
        price = request.POST.get('price')
        edition = request.POST.get('edition')

        Book.objects.create(
            title=title,
            author=author,
            price=price,
            edition=edition
        )
        return redirect('lab9_part1.listbooks')

    return render(request, 'bookmodule/lab9_part1_addbook.html')


def lab9_part1_editbook(request, id):
    book = get_object_or_404(Book, id=id)

    if request.method == "POST":
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.price = request.POST.get('price')
        book.edition = request.POST.get('edition')
        book.save()
        return redirect('lab9_part1.listbooks')

    return render(request, 'bookmodule/lab9_part1_editbook.html', {'book': book})

def lab9_part1_deletebook(request, id):
    book = get_object_or_404(Book, id=id)
    book.delete()
    return redirect('lab9_part1.listbooks')



from .forms import BookForm  # لازم نستورد BookForm

# ✅ عرض جميع الكتب
def lab9_part2_listbooks(request):
    books = Book.objects.all()
    return render(request, 'bookmodule/lab9_part2_listbooks.html', {'books': books})

# ✅ إضافة كتاب جديد
def lab9_part2_addbook(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lab9_part2.listbooks')
    else:
        form = BookForm()
    return render(request, 'bookmodule/lab9_part2_addbook.html', {'form': form})

# ✅ تعديل بيانات كتاب
def lab9_part2_editbook(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('lab9_part2.listbooks')
    else:
        form = BookForm(instance=book)
    return render(request, 'bookmodule/lab9_part2_editbook.html', {'form': form, 'book': book})

# ✅ حذف كتاب
def lab9_part2_deletebook(request, id):
    book = get_object_or_404(Book, id=id)
    book.delete()
    return redirect('lab9_part2.listbooks')


#Lab 11
from django.shortcuts import render, redirect, get_object_or_404
from .forms import StudentForm, AddressForm
from .models import Student, Address
from apps.bookmodule.models import Address


# ✅ List Students
@login_required
def student_list(request):
    students = Student.objects.all()
    return render(request, 'bookmodule/lab11_student_list.html', {'students': students})

# ✅ Add Student + Address
@login_required
def student_add(request):
    if request.method == 'POST':
        s_form = StudentForm(request.POST)
        a_form = AddressForm(request.POST)
        if s_form.is_valid() and a_form.is_valid():
            address = a_form.save()  # Always creates a new Address object
            student = s_form.save(commit=False)
            student.address = address
            student.save()
            return redirect('student_list')
    else:
        s_form = StudentForm()
        a_form = AddressForm()
    return render(request, 'bookmodule/lab11_add_student.html', {'s_form': s_form, 'a_form': a_form})


# ✅ Edit Student + Address
@login_required
def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    address = student.address
    s_form = StudentForm(request.POST or None, instance=student)
    a_form = AddressForm(request.POST or None, instance=address)
    if request.method == 'POST' and s_form.is_valid() and a_form.is_valid():
        a_form.save()
        s_form.save()
        return redirect('student_list')
    return render(request, 'bookmodule/lab11_edit_student.html', {'s_form': s_form, 'a_form': a_form})

# ✅ Delete Student
@login_required
def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'bookmodule/lab11_delete_student.html', {'student': student})


@login_required
def student2_list(request):
    students = Student2.objects.all()
    return render(request, 'bookmodule/student2_list.html', {'students': students})

@login_required
def student2_add(request):
    if request.method == 'POST':
        form = Student2Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student2_list')
    else:
        form = Student2Form()
    return render(request, 'bookmodule/student2_add.html', {'form': form})


@login_required
def gallery_upload(request):
    if request.method == 'POST':
        form = GalleryItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('gallery_upload')
    else:
        form = GalleryItemForm()
    return render(request, 'bookmodule/gallery_upload.html', {'form': form})

