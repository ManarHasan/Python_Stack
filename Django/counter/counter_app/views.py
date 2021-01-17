from django.shortcuts import render, redirect
def index(request):


    if 'counter' in request.session:
        request.session['counter'] += 1
    else:
        request.session['counter'] = 0
    if 'visits' in request.session:
        request.session['visits'] += 1
    else:
        request.session['visits'] = 0
    return render(request, 'index.html')
def destroy(request):
    del request.session['counter']
    return redirect("/")
def plus_2(request):
    request.session['counter'] += 1
    return redirect("/")
def user_add(request):
    if request.method == "POST":
        request.session['counter'] += int(request.POST['increment']) - 1
    return redirect("/")