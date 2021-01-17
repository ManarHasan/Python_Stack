from django.shortcuts import render, redirect
import random


def result(request):
    if 'visits' not in request.session:
        request.session['username'] = []
        request.session['attempts'] = []
        request.session['visits'] = 0
    if 'counter' not in request.session:
        request.session['counter'] = 0
    if 'user' not in request.session:
        request.session['user'] = 3
    if 'user_input' not in request.session:
        request.session['result'] = random.randint(1, 100)
        print(request.session['result'])
    print(request.session['result'])
    return render(request, 'index.html')


def user_input(request):
    if request.method == "POST":
        request.session['user_input'] = int(request.POST['user'])
        if request.session['user_input'] < request.session['result']:
            request.session['user'] = 0
        if request.session['user_input'] > request.session['result']:
            request.session['user'] = 1
        if request.session['user_input'] == request.session['result']:
            request.session['user'] = 2
        if request.session['counter'] == 4:
            request.session['user'] = 4
        request.session['counter'] += 1
        return redirect("/")


def leaderboard(request):
    if request.method == "GET":
        request.session['visits'] += 1
        request.session['username'].append(request.GET['username'])
        request.session['attempts'].append(request.session['counter'])

    return render(request, 'leaderboard.html')


def destroy(request):
    del request.session['user_input']
    del request.session['user']
    del request.session['result']
    del request.session['counter']
    return redirect("/")
