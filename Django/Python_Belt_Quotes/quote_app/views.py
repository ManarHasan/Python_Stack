from django.shortcuts import render, redirect
import bcrypt
from . import models
from django.contrib import messages
import re


def home_page(request):
    return render(request, 'home_page.html')


def validate_text(text, min_length=2):
    if text.isalpha == False:
        return 0
    elif len(text) < min_length:
        return 1
    elif len(text) > min_length:
        return 2


def validate_email(email):
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if re.search(regex, email):
        if not models.is_duplicate_email(email):
            return 0
        return 1
    return 2


def register(request):
    if request.method == 'POST':
        password = request.POST['password']
        pw_hash = bcrypt.hashpw(
            password.encode(), bcrypt.gensalt()).decode()
        errors = models.user_validator(
            request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
                return redirect('/')
        if validate_text(request.POST['fname']) == 2 and validate_text(request.POST['lname']) and validate_text(request.POST['password'], min_length=8) == 2 \
                and validate_email(request.POST['email']) == 0 and request.POST['password'] == request.POST['confirm']:
            user = models.insert_new_user(
                request.POST['fname'], request.POST['lname'], request.POST['email'], pw_hash)
            if 'user_id' not in request.session:
                request.session['user_id'] = user.id
                request.session['first_name'] = user.first_name
                request.session['last_name'] = user.last_name
            return redirect('/quotes')


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        user = models.get_user(email)
        if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
            if user is not None:
                if 'user_id' not in request.session:
                    request.session['user_id'] = user.id
                    request.session['first_name'] = user.first_name
                    request.session['last_name'] = user.last_name
                return redirect('/quotes')
    return redirect('/')


def user_account(request, user_id):
    user = models.get_user_by_id(user_id)
    all_quotes = models.all_quotes_owned(user_id)
    print(all_quotes)
    context = {
        "user": user,
        "all_quotes": all_quotes
    }
    return render(request, "user_account.html", context)


def my_account(request, user_id):
    context = {
        "user": models.get_user_by_id(user_id)
    }
    return render(request, "my_account.html", context)


def edit_account(request, user_id):
    errors = models.user_edit_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
            return redirect('/myaccount/'+str(user_id))
    user = models.edit_account(request.POST, user_id)
    request.session['first_name'] = user.first_name
    request.session['last_name'] = user.last_name
    return redirect('/myaccount/'+str(user_id))


def logout(request):
    if 'user_id' in request.session:
        del request.session['user_id']
        del request.session['first_name']
        del request.session['last_name']
    return redirect('/')


def quotes(request):
    context = {
        "user": models.get_user_by_id(request.session['user_id']),
        "all_quotes": models.all_quotes()
    }
    return render(request, "quotes.html", context)


def add_quote(request):
    if request.method == 'POST':
        errors = models.quote_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
                return('/quotes')
        quote = models.insert_new_quote(
            request.POST['author'], request.POST['quote'], request.session['user_id'])
        models.like_quote(
            quote.id, request.session['user_id'])
        return redirect('/quotes')


def like_quote(request, quote_id, user_id):
    add = models.like_quote(quote_id, user_id)
    return redirect('/quotes')


def dislike_quote(request, quote_id, user_id):
    remove = models.dislike_quote(quote_id, user_id)
    return redirect('/quotes')


def delete_quote(request, quote_id):
    quote = models.delete_quote(quote_id)
    return redirect('/quotes')
