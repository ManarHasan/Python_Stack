from django.shortcuts import render, redirect
import bcrypt
from .models import User
from django.contrib import messages
import re
import datetime


def index(request):
    return render(request, "index.html")


def add_user(request):
    if request.method == 'POST':
        EMAIL_REGEX = re.compile(
            r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        errors = {}
        today = datetime.datetime.now().strftime("%Y%m%d")
        user_birthday = request.POST['date'].replace("-", "")
        if request.POST['which_form'] == 'register':
            if request.POST['confirm'] != request.POST['password']:
                errors["confirm"] = "The passwords do not match"
                if len(errors) > 0:
                    for key, value in errors.items():
                        messages.error(request, value)
                        return redirect('/')
            if len(request.POST['fname']) < 2:
                errors["fname"] = "This name is too short go to court and change your name"
                if len(errors) > 0:
                    for key, value in errors.items():
                        messages.error(request, value)
                        return redirect('/')
            if len(request.POST['lname']) < 2:
                errors["lname"] = "This name is too short go to court and change your name"
                if len(errors) > 0:
                    for key, value in errors.items():
                        messages.error(request, value)
                        return redirect('/')
            if not EMAIL_REGEX.match(request.POST['email']):
                errors['email'] = "Invalid email address!"
                if len(errors) > 0:
                    for key, value in errors.items():
                        messages.error(request, value)
                        return redirect('/')
            all_users_emails = User.objects.all().values_list('email', flat=True)
            for i in all_users_emails:
                if i == request.POST['email']:
                    errors['email'] = "This email already exists"
                    if len(errors) > 0:
                        for key, value in errors.items():
                            messages.error(request, value)
                            return redirect('/')
            if len(request.POST['password']) < 8:
                errors["password"] = "This password is too short"
                if len(errors) > 0:
                    for key, value in errors.items():
                        messages.error(request, value)
                        return redirect('/')
            if user_birthday > today:
                errors["date"] = "You can't be born in the future??????????"
                if len(errors) > 0:
                    for key, value in errors.items():
                        messages.error(request, value)
                        return redirect('/')
            if (int(today[0:4]) - int(user_birthday[0:4])) <= 13:
                errors['date'] = "You are too young????????????????????????????????????"
                if len(errors) > 0:
                    for key, value in errors.items():
                        messages.error(request, value)
                        return redirect('/')
            password = request.POST['password']
            pw_hash = bcrypt.hashpw(
                password.encode(), bcrypt.gensalt()).decode()
            new_user = User.objects.create(first_name=request.POST['fname'], last_name=request.POST['lname'],
                                           email=request.POST['email'], birthday=request.POST['date'], password=pw_hash, confirm=pw_hash)
            return redirect('/success/'+str(new_user.id))
        if request.POST['which_form'] == 'login':
            user = User.objects.get(email=request.POST['email'])
            if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
                return redirect("/success/"+str(user.id))
            else:
                errors['password'] = "incorrect password"
                if len(errors) > 0:
                    for key, value in errors.items():
                        messages.error(request, value)
                        return redirect('/')


def success(request, id):
    if 'is_login' not in request.session:
        request.session['is_login'] = 1
    context = {
        "users": User.objects.get(id=id)
    }
    return render(request, 'success.html', context)


def delete(request):
    del request.session['is_login']
    return redirect('/')
