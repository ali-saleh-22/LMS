from django.urls import path, include
from users.views import *
from django.contrib.auth.views import PasswordChangeDoneView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('profile/', profile, name='profile'),
    path('profile/<int:id>/', profile_account, name='profile.account'),
    path('register_student/', register_student, name='register.student'),
    path('register_staff/', register_staff, name='register.staff'),
    path('edit_profile/', edit_profile, name='profile.edit'),
    path('change_password/', change_password.as_view(), name='change_password'),
    path('done_change_password/', PasswordChangeDoneView.as_view(), name='done_change_password'),
    path('students/', student_list, name='students.index'),
    path('borrowd/books/', borrowed_books, name='books.borrowed')

]
