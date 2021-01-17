from django.db import models
import bcrypt


class User(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    birthday = models.DateTimeField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Wish(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    users = models.ManyToManyField(User, related_name="wishes")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


def register_validator(postData):
    errors = {}
    if postData['name'].isalpha == False:
        errors['name'] = 'Name must be letter unlucky Elon'
    if len(postData['name']) < 2:
        errors['name'] = 'Name must be at least 3 characters'
    if len(postData['username']) < 5:
        errors['username'] = 'Username must be at least 5 characters'
    if len(postData['password']) < 8:
        errors['password'] = 'Password must be at least 8 characters'
    if postData['confirm'] != postData['password']:
        errors['confirm'] = "Passwords don't match"
    return errors


def add_user(postData):
    pw_hash = bcrypt.hashpw(
        postData['password'].encode(), bcrypt.gensalt()).decode()
    user = User.objects.create(
        name=postData['name'], username=postData['username'], password=pw_hash, birthday=postData['date'])
    return user


def get_user(username):
    user = User.objects.filter(username=username)
    return user


def wish_validator(postData):
    errors = {}
    if len(postData['title']) < 5:
        errors['title'] = 'Title must be at least 5 characters'
    if len(postData['desc']) < 10:
        errors['desc'] = 'Description must be at least 10 characters'
    return errors


def add_new_wish(user_id, title, desc):
    new_wish = Wish.objects.create(
        title=title, desc=desc)
    user = User.objects.get(id=user_id)
    new_wish.users.add(user)
    return new_wish


def add_wish(user_id, wish_id):
    user = User.objects.get(id=user_id)
    wish = Wish.objects.get(id=wish_id)
    add_wish = wish.users.add(user)
    return add_wish


def remove_wish(user_id, wish_id):
    user = User.objects.get(id=user_id)
    wish = Wish.objects.get(id=wish_id)
    add_wish = wish.users.remove(user)
    return add_wish
