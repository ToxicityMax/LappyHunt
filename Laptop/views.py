from django.shortcuts import render
from django.contrib.auth.models import User
from .models import *
from django.http import Http404, JsonResponse
from django.shortcuts import redirect
from json import loads
from django.contrib.auth import authenticate, login as dj_login



def home(request):
    return render(request, "Laptop/index.html")


def laptop(request):
    if request.method == "GET":
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


#def detail(request, slug):
#    spec = LaptopSpec.objects.filter(slug__iexact=slug)
#    if spec.exists():
#        spec = spec.first()
#    else:
#        return HttpResponse("<h1>Post Not Found</h1>")
#    context = {
#        "spec": spec,
#    }
#    return render(request, "Laptop/specific_view.html", context)

def detail(request):
    return render(request,"Laptop/specificview.html")

def cart(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            customer = request.user.customer
            print(customer)
            cart, created = Cart.objects.get_or_create(customer=customer)
            print(cart, created)
            items = cart.cartitem_set.all()
            return render(request, "Laptop/cart.html", {"items": items})
        else:
            return redirect('HOME')


def updateitem(request):
    data = loads(request.body)
    laptopId = data["productId"]
    action = data["action"]
    customer = request.user.customer
    laptop = LaptopSpec.objects.get(id=laptopId)
    if action == "add":
        cart, created = Cart.objects.get_or_create(customer=customer)
        cartitem, created = cartItem.objects.get_or_create(
            laptop=laptop, cart=cart)
        return JsonResponse("item was added", safe=False)
    elif action == "delete":
        cart = customer.cart_set.all()
        cart[0].cartitem_set.filter(laptop=laptop).delete()
        return JsonResponse("Item was deleted")

def login(request):
        if request.method == 'GET':
            return render(request,"laptop/login.html")
        else:
            email = request.POST["email"]
            username = email.split("@")
            password = request.POST["password"]
            user,created = User.objects.get_or_create(username=username[0])
            
            if created:
                user.password = password
                user.save()
                customer= Customer.objects.create(user=user,email=email)
                customer.save()
                dj_login(request, user)
                return redirect("CART")
            else:
                user = authenticate(request,username=username[0], password=password)
                if user is not None:
                    dj_login(request, user)
                    return redirect("CART")
                else:
                    #password incorrect
                    return render(request,"laptop/login.html",{"error":"Incorrect Password"})