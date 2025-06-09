from django import forms
from books.models import Book, Borrow


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'


class BorrowBookForm(forms.ModelForm):
    class Meta:
        model = Borrow
        fields = ['book']