from django import forms
from .models import Book, Student, Address

class BookForm(forms.ModelForm):  # From Lab 10
    class Meta:
        model = Book
        fields = ['title', 'author', 'price', 'edition']

from django import forms
from .models import Student, Address

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age']  # Not 'address'

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['street', 'city', 'zipcode']


from .models import Student2, Address2
from django import forms

class Address2Form(forms.ModelForm):
    class Meta:
        model = Address2
        fields = ['street', 'city', 'zipcode']

class Student2Form(forms.ModelForm):
    class Meta:
        model = Student2
        fields = ['name', 'age', 'addresses']
        widgets = {
            'addresses': forms.CheckboxSelectMultiple
        }


from .models import GalleryItem

class GalleryItemForm(forms.ModelForm):
    class Meta:
        model = GalleryItem
        fields = ['title', 'image']
