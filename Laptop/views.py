from django.shortcuts import render
from .models import *
from django.http import Http404,JsonResponse
from django.shortcuts import redirect
from json import loads

def home(request):
    return render(request, "Home/index.html")


def laptop(request):
    if request.method == "GET":
        if request.GET.getlist("search"):
            order = request.GET.getlist("search")
            lap_list = LaptopSpec.objects.order_by(*order)
            context = {"lap_list": lap_list}
            return render(request, "specs/main.html", context)
        else:
            lap_list = LaptopSpec.objects.order_by("id")    
            context = {"lap_list": lap_list}
            return render(request, "specs/main.html", context)
    else:
        query = request.POST["search"]
        specs = LaptopSpec.objects.filter(DisplayName__icontains=query)
        param = {"lap_list": specs, "query": query}
        return render(request, "specs/main.html", param)


def detail(request, slug):

    spec = LaptopSpec.objects.filter(slug__iexact=slug)
    if spec.exists():
        spec = spec.first()
    else:
        return HttpResponse("<h1>Post Not Found</h1>")
    context = {
        "spec": spec,
    }
    return render(request, "specs/details.html", context)


def cart(request):
    if request.method=='GET':
        if request.user.is_authenticated:
            customer = request.user.customer
            cart,created = Cart.objects.get_or_create(customer=customer)
            items = cart.cartitem_set.all()
            return render(request, "cart.html",{"items":items})
        else:
            return redirect('HOME')
def updateitem(request):
    data = loads(request.body)
    laptopId = data["productId"]
    action = data["action"]
    print(data)
    customer = request.user.customer
    laptop = LaptopSpec.objects.get(id=laptopId)
    cart,created = Cart.objects.get_or_create(customer=customer)
    cartitem,created = cartItem.objects.get_or_create(laptop=laptop,cart=cart)
    return JsonResponse("item was added",safe=False)