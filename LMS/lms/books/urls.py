from django.urls import path
from books.views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', index, name='books.index'),
    path('<int:id>/', show, name='books.show'),
    path('delete/<int:id>/', delete, name='books.delete'),
    path('create/', login_required(create.as_view()), name='books.create'),
    path('update/<int:pk>/', login_required(update.as_view()), name='books.update'),
    path('borrow_book/<int:id>/', borrow_book, name='books.borrow'),
    path('student_borrowed_books/', student_borrowed_books, name='books.borrowed.student'),
    path('return_book/<int:id>/', return_book, name='books.return')
]
