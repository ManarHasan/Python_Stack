from django.shortcuts import render, redirect
from .models import Dojos, Ninjas


def index(request):
    context = {
        "Dojos": Dojos.objects.all()
    }
    return render(request, "index.html", context)


def add_dojo(request):
    Dojos.objects.create(
        name=request.POST['name'], city=request.POST['city'], state=request.POST['state'])
    return redirect("/")


def add_ninja(request):
    dojo_id = request.POST['dojos']
    Ninjas.objects.create(
        dojo=Dojos.objects.get(id=dojo_id), first_name=request.POST['first_name'], last_name=request.POST['last_name'])
    return redirect("/")


def delete(request, i="<i>"):
    dojo_id = i
    dojo_to_delete = Dojos.objects.get(id=dojo_id)
    dojo_to_delete.delete()
    return redirect("/")
