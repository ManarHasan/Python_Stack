from django.shortcuts import render, redirect
from .models import Order, Product


def index(request):
    if 'quantity' not in request.session:
        request.session["quantity"] = 0
        request.session["price"] = 0
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)


def add(request):
    request.session["quantity"] += int(request.POST["quantity"])
    request.session["price"] += float(request.POST["price"])
    return redirect('/')


def checkout(request):
    print("Charging credit card...")
    if 'checkout' not in request.session:
        request.session['checkout'] = 0
        order = Order.objects.create(
            quantity_ordered=request.session["quantity"], total_price=request.session["price"])
        context = {
            "order": order
        }
        return render(request, "store/checkout.html", context)
    if 'checkout' in request.session:
        order = Order.objects.create(
            quantity_ordered=request.session["quantity"], total_price=request.session["price"])
        return redirect('/delete/'+str(order.id))


def delete(request, i):
    del request.session["price"]
    del request.session["quantity"]
    del request.session['checkout']
    delete = Order.objects.get(id=i)
    delete.delete()
    return redirect("/")
