from django.shortcuts import render, redirect


def dojo(request):
    return render(request, "dojo.html")


def submit(request):
    fname = request.POST['fname']
    lname = request.POST['lname']
    location = request.POST['location']
    lang = request.POST['lang']
    comment = request.POST["comment"]
    checkbox = request.POST['check']
    radio_yes = request.POST['yes']
    radio_hyes = request.POST['hyes']

    context = {
        "fname": fname,
        "lname": lname,
        "location": location,
        "lang": lang,
        "comment": comment,
        "checkbox": checkbox,
        "radio_yes": radio_yes,
        "radio_hyes": radio_hyes
    }
    return render(request, "result.html", context)
