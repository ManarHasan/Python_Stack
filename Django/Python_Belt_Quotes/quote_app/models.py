from django.db import models
from . import views


class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Quote(models.Model):
    author = models.CharField(max_length=255)
    quote = models.TextField()
    owner = models.ForeignKey(
        User, related_name="quotes", on_delete=models.CASCADE)
    users_who_liked = models.ManyToManyField(User, related_name="quote_liked")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


def user_validator(postData):
    errors = {}
    if views.validate_text(postData['fname']) == 0:
        errors["first_name_1"] = "First name should be letters not numbers! Sorry Elon Musk's baby!"
    if views.validate_text(postData['fname']) == 1:
        errors["first_name_2"] = "First name should be at least 2 characters"
    if views.validate_text(postData['lname']) == 0:
        errors["last_name_1"] = "Last name should be letters not numbers! Sorry Elon Musk's baby!"
    if views.validate_text(postData['lname']) == 1:
        errors["last_name_2"] = "Last name should be at least 2 characters"
    if views.validate_text(postData['password'], min_length=8) == 1:
        errors["password"] = "Password should be at least 8 characters"
    if views.validate_email(postData['email']) == 2:
        errors["email_1"] = "Invalid email!"
    if views.validate_email(postData['email']) == 1:
        errors["email_2"] = "Email already exists!"
    if postData['password'] != postData['confirm']:
        errors["password"] = "Passwords do not match!"
    return errors


def user_edit_validator(postData):
    errors = {}
    if views.validate_text(postData['fname']) == 0:
        errors["first_name_1"] = "First name should be letters not numbers! Sorry Elon Musk's baby!"
    if views.validate_text(postData['fname']) == 1:
        errors["first_name_2"] = "First name should be at least 2 characters"
    if views.validate_text(postData['lname']) == 0:
        errors["last_name_1"] = "Last name should be letters not numbers! Sorry Elon Musk's baby!"
    if views.validate_text(postData['lname']) == 1:
        errors["last_name_2"] = "Last name should be at least 2 characters"
    if views.validate_email(postData['email']) == 2:
        errors["email_1"] = "Invalid email!"
    if views.validate_email(postData['email']) == 1:
        errors["email_2"] = "Email already exists!"
    return errors


def insert_new_user(first_name, last_name, email, password):
    user = User.objects.create(
        first_name=first_name, last_name=last_name, email=email, password=password)
    return user


def is_duplicate_email(email):
    users = User.objects.filter(email=email).values()
    if len(users):
        return True
    return False


def get_user(email):
    users = User.objects.filter(email=email)
    if not len(users):
        return None
    return users[0]


def get_user_by_id(id):
    user = User.objects.get(id=id)
    return user


def quote_validator(postData):
    errors = {}
    if views.validate_text(postData['author'], min_length=3) == 1:
        errors['author'] = "Author must be at least 3 characters"
    if views.validate_text(postData['quote'], min_length=10) == 1:
        errors['quote'] = "Quote should be at least 10 characters"
    return errors


def insert_new_quote(author, quote, id):
    quote = Quote.objects.create(
        author=author, quote=quote, owner=(User.objects.get(id=id)))
    return quote


def get_quote(id):
    quote = Quote.objects.get(id=id)
    return quote


def all_quotes():
    all_quotes = Quote.objects.all()
    return all_quotes


def like_quote(quote_id, user_id):
    quote = Quote.objects.get(id=quote_id)
    user = User.objects.get(id=user_id)
    quote.users_who_liked.add(user)
    return True


def dislike_quote(quote_id, user_id):
    quote = Quote.objects.get(id=quote_id)
    user = User.objects.get(id=user_id)
    quote.users_who_liked.remove(user)
    return True


def delete_quote(quote_id):
    quote = Quote.objects.get(id=quote_id)
    quote.delete()
    return True


def edit_account(postData, user_id):
    user = User.objects.get(id=user_id)
    user.first_name = postData['fname']
    user.last_name = postData['lname']
    user.email = postData['email']
    user.save()
    return user


def all_quotes_owned(user_id):
    user = User.objects.get(id=user_id)
    all_quotes = user.quotes.all()
    return all_quotes
