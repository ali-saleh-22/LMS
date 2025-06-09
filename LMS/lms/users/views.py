from django.shortcuts import render, redirect, reverse, get_object_or_404
from users.forms import EditProfileForm, RegisterForm
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth import login
from books.models import Borrow
from users.models import CustomUser


def is_staff(user):
    return user.is_staff


def register_student(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_student = True
            user.save()
            login(request, user)
            url = reverse('books.index')
            return redirect(url)
    else:
        form = RegisterForm()
    return render(request, 'users/register_student.html', {'form': form})


def register_staff(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_mod = True
            user.is_staff = True
            user.save()
            # login(request, user)
            url = reverse('books.index')
            return redirect(url)
    else:
        form = RegisterForm()
    return render(request, 'users/register_staff.html', {'form': form})


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('books.index')
    else:
        form = EditProfileForm(instance=request.user)
    return render(request, 'users/edit_profile.html', {'form': form})


@login_required()
def profile(request):
    url = reverse('profile.account', args=[request.user.id])
    return redirect(url)


@login_required()
def profile_account(request, id):
    account = get_object_or_404(CustomUser, id=id)
    return render(request, 'users/account_profile.html', {'account': account})


class change_password(PasswordChangeView):
    template_name = 'users/change_password.html'
    success_url = '/'


@login_required
def student_list(request):
    name = request.GET.get('name')
    students = CustomUser.objects.filter(is_student=True)
    if name:
        students = students.filter(username__icontains=name)
    return render(request, 'users/student_list.html', {'students': students})


@login_required()
def borrowed_books(request):
    borrows = Borrow.objects.all()
    students = CustomUser.objects.filter(is_student=True)
    return render(request, 'users/borrowed_books.html', {'borrows': borrows, 'students': students})
