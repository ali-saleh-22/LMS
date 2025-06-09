from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views.generic import CreateView, UpdateView
from books.models import Book, Borrow
from books.forms import BookForm
from django.contrib.auth.decorators import login_required
from datetime import date, timedelta
from django.utils import timezone


@login_required()
def index(request):
    books = Book.objects.all().order_by('-id')
    return render(request, 'books/index.html', {'books': books})


@login_required()
def show(request, id):
    book = get_object_or_404(Book, id=id)
    return render(request, 'books/show.html', {'book': book})


class create(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'books/create.html'
    success_url = '/'


class update(UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'books/update.html'
    success_url = '/'


@login_required()
def delete(request, id):
    book = get_object_or_404(Book, id=id)
    book.delete()
    url = reverse('books.index')
    return redirect(url)


def student_borrowed_books(request):
    student_email = request.user.email
    borrowed_books = Borrow.objects.filter(student_email=student_email)
    return render(request, 'books/student_borrowed_books.html', {'borrowed_books': borrowed_books})


def borrow_book(request, id):
    book = get_object_or_404(Book, id=id)
    if not book.is_borrowed:
        student_email = request.user.email
        Borrow.objects.create(
            book=book,
            student_email=student_email,
            return_date=timezone.now() + timedelta(days=1))
        book.is_borrowed = True
        book.save()
    url = reverse('books.index')
    return redirect(url)


@login_required
def return_book(request, id):
    borrow_record = get_object_or_404(Borrow, id=id, student_email=request.user.email)
    book = borrow_record.book
    book.is_borrowed = False
    book.save()
    borrow_record.delete()
    url = reverse('books.index')
    return redirect(url)
