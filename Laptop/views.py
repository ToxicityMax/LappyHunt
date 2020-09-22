from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout as dj_logout, login as dj_login
from .models import *
from django.http import Http404, JsonResponse
from json import loads
from django.contrib import messages


def home(request):
    return render(request, "Laptop/index.html")


def laptop(request):
    if request.method == "GET":
        print(request.user)
        if request.GET.getlist("search"):
            order = request.GET.getlist("search")
            lap_list = LaptopSpec.objects.order_by(*order)
            context = {"lap_list": lap_list}
            return render(request, "Laptop/list.html", context)
        else:
            lap_list = LaptopSpec.objects.order_by("id")
            context = {"lap_list": lap_list}
            return render(request, "Laptop/list.html", context)
    else:
        query = request.POST["search"]
        specs = LaptopSpec.objects.filter(DisplayName__icontains=query)
        param = {"lap_list": specs, "query": query}
        return render(request, "Laptop/list.html", param)


def detail(request, slug):
    spec = get_object_or_404(LaptopSpec, slug=slug)
    return render(request, 'Laptop/specificview.html', {'spec': spec})


def cart(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            user = request.user
            print(user)
            cart, created = Cart.objects.get_or_create(user=user)
            print(cart, created)
            items = cart.cartitem_set.all()
            return render(request, "Laptop/cart.html", {"items": items})
        else:
            return redirect('HOME')


def updateitem(request):
    data = loads(request.body)
    laptopId = data["productId"]
    action = data["action"]
    user = request.user
    laptop = LaptopSpec.objects.get(id=laptopId)
    if action == "add":
        cart, created = Cart.objects.get_or_create(user=user)
        if cart.add():
            cartitem, created = cartItem.objects.get_or_create(
                laptop=laptop, cart=cart)
            return JsonResponse("Item was added",safe=True)

        else:
            messages.success(request, 'Cannot add more items')
            return JsonResponse("Cannot add more items",safe=True)

    elif action == "delete":
        cart = user.cart_set.get(user=user)
        cart.cartitem_set.filter(laptop=laptop).delete()
        if cart.delete():
            messages.success(request, 'Item was deleted.')
            return JsonResponse("Item was deleted",safe=True)
        else:
            messages.success(request, 'Cart Empty')
            return JsonResponse({"message": "Cart Empty"})


def login(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('LAPTOP')
        else:
            return render(request, "Laptop/login.html")
    else:
        username = request.POST["email"]
        email = username
        password = request.POST["password"]
        try:
            user = User.objects.get(username=username)
            user = authenticate(request, username=username,
                                email=email, password=password)
            if user is not None:
                dj_login(request, user)
                messages.success(request, 'You are logged in.')
                return redirect("LAPTOP")
            else:
                return render(request, "Laptop/login.html", {"error": "Incorrect Password"})
        except User.DoesNotExist:
            user = User.objects.create_user(
                username=username, email=email, password=password)
            user.save()
            dj_login(request, user)
            messages.success(request, 'You are logged in.')
            return redirect('LAPTOP')


def logout(request):
    print(request.user)
    dj_logout(request)
    messages.success(request, 'You were logged out.')
    return redirect("LAPTOP")
