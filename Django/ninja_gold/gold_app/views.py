from django.shortcuts import render, redirect
import random


def index(request):
    if 'start' not in request.session:
        request.session['start'] = 1
    if 'gold' not in request.session:
        request.session['gold'] = 0
        request.session['moves'] = 0
        request.session['results'] = []
    return render(request, 'index.html')


def add_rules(request):
    request.session['moves_lose'] = int(request.POST['moves'])
    request.session['gold_goal'] = int(request.POST['gold_win'])
    request.session['start'] = 0
    return redirect('/')


def process_money(request, name):
    which_button = name
    if which_button == 'farm':
        request.session['result'] = random.randint(10, 20)
        request.session['gold'] += int(request.session['result'])
        request.session['moves'] += 1
        request.session['results'].append(
            "You earned " + str(request.session['result']))
    if which_button == 'cave':
        request.session['result'] = random.randint(5, 10)
        request.session['gold'] += int(request.session['result'])
        request.session['moves'] += 1
        request.session['results'].append(
            "You earned " + str(request.session['result']))
    if which_button == 'house':
        request.session['result'] = random.randint(2, 5)
        request.session['gold'] += int(request.session['result'])
        request.session['moves'] += 1
        request.session['results'].append(
            "You earned " + str(request.session['result']))
    if which_button == 'casino':
        request.session.earn_or_lose = random.randint(1, 2)
        if request.session.earn_or_lose is 1:
            request.session['result'] = random.randint(0, 50)
            request.session['gold'] += int(request.session['result'])
            request.session['moves'] += 1
            request.session['results'].append(
                "You earned " + str(request.session['result']))
        if request.session.earn_or_lose is 2:
            request.session['result'] = random.randint(0, 50)
            request.session['gold'] -= int(request.session['result'])
            request.session['moves'] += 1
            request.session['results'].append(
                "You lost " + str(request.session['result']))
    if request.session['moves'] == request.session['moves_lose']:
        return redirect('/lose')
    if int(request.session['gold']) >= int(request.session['gold_goal']):
        return redirect('/win')
    return render(request, "index.html")


def win(request):
    return render(request, "win.html")


def lose(request):
    return render(request, "lose.html")


def delete(request):
    del request.session['gold']
    del request.session['result']
    del request.session['results']
    del request.session['start']
    del request.session['moves']
    del request.session['moves_lose']
    del request.session['gold_goal']
    return redirect('/')
