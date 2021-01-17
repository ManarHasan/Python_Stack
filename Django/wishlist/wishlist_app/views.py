from django.shortcuts import render, redirect
from . import models
from .models import User, Wish
import bcrypt


def home_page(request):
    return render(request, "index.html")


def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        username = request.POST['username']
        errors = models.register_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        user = models.add_user(request.POST)
        if 'user' not in request.session:
            request.session['username'] = username
            request.session['name'] = name
            request.session['user_id'] = user.id
        return redirect('/welcome/'+str(user.id))


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        user = models.get_user(username)
        print(user)
        if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
            if 'user' not in request.session:
                request.session['username'] = username
                request.session['name'] = name
                request.session['user_id'] = user.id
            return redirect('/welcome/'+str(user.id))
        errors = {
            'login': 'Incorrect username or password'
        }
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')


def logout(request):
    del request.session['username']
    del request.session['name']
    del request.session['user_id']
    return redirect('/')


def welcome(request, id):
    all_users = User.objects.all()
    all_wishes = Wish.objects.all()
    user = User.objects.get(id=id)
    all_user_wishes = user.wishes.all()
    context = {
        "all_users": all_users,
        "all_wishes": all_wishes,
        "user": user,
        "all_user_wishes": all_user_wishes
    }
    return render(request, 'welcome.html', context)


def new_wish_page(request):
    return render(request, 'new_wish.html')


def new_wish(request, user_id):
    if request.method == 'POST':
        title = request.POST['title']
        desc = request.POST['desc']
        errors = models.wish_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/new_wish/'+str(user_id))
        new_wish = models.add_new_wish(user_id, title, desc)
        return ('/welcome/'+str(user_id))


def add(request, user_id, wish_id):
    models.add_wish(user_id, wish_id)
    return redirect('/welcome/'+str(user_id))


def remove(request, user_id, wish_id):
    models.remove_wish(user_id, wish_id)
    return redirect('/welcome/'+str(user_id))
