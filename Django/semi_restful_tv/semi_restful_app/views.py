from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Showtime


def new_show(request):
    return render(request, "index.html")


def root(request):
    return redirect('/shows')


def add_show(request):
    errors = Showtime.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
            return redirect('shows/new')
    else:
        Showtime.objects.create(title=request.POST['title'], network=request.POST['network'],
                                release_date=request.POST['date'], desc=request.POST['desc'])
        return redirect('/shows')


def all_shows(request):
    context = {
        "all_shows": Showtime.objects.all()
    }
    return render(request, "shows.html", context)


def edit_page(request, i):
    context = {
        "show": Showtime.objects.get(id=i)
    }
    return render(request, "edit.html", context)


def edit(request, i):
    errors = Showtime.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
            return redirect('/edit/'+str(i))
    else:
        show = Showtime.objects.get(id=i)
        show.title = request.POST['title']
        show.network = request.POST['network']
        show.release_date = request.POST['date']
        show.desc = request.POST['desc']
        show.save()
        return redirect('/')


def profile(request, i):
    context = {
        "show": Showtime.objects.get(id=i)
    }
    return render(request, "show_profile.html", context)


def delete(request, i):
    show = Showtime.objects.get(id=i)
    show.delete()
    return redirect("/")
