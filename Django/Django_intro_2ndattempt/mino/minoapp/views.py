# add redirect to import statement
from django.shortcuts import HttpResponse, redirect, render
from django.http import JsonResponse


def root_method(request):
    return HttpResponse("String response from root_method")


def another_method(request):
    return redirect("/redirected_route")


def redirected_method(request):
    return JsonResponse({"response": "JSON response from redirected_method", "status": True})


def index(request):
    context = {
        "name": "Noelle",
        "favorite_color": "turquoise",
        "pets": ["Bruce", "Fitz", "Georgie"]
    }
    return render(request, "index.html", context)
