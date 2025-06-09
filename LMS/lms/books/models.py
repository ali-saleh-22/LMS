from django.db import models
from django.shortcuts import reverse


class Book(models.Model):
    name = models.CharField(max_length=30)
    author = models.CharField(max_length=20)
    published_year = models.PositiveIntegerField()
    description = models.TextField(null=True, blank=True)
    is_borrowed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name}'

    def update_url(self):
        url = reverse('books.update', args=[self.id])
        return url

    def delete_url(self):
        url = reverse('books.delete', args=[self.id])
        return url

    def show_url(self):
        url = reverse('books.show', args=[self.id])
        return url


class Borrow(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    student_email = models.EmailField(null=True, blank=True)
    borrow_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(null=True)
