from django.shortcuts import HttpResponse, render
from time import gmtime, strftime
from datetime import date


def root(request):
    context = {
        "time": strftime("%Y-%m-%d %H:%M %p", gmtime())
    }
    return render(request, 'index.html', context)


def index(request):

    return render(request, 'new_time.html')
