from django.shortcuts import render
from .models import LaptopSpec
from django.http import HttpResponse, Http404


def home(request):
    return render(request, "Home/index.html")


def laptop(request):
    if request.method == "GET":
        try:
            order = request.GET["order"]
            print(order)
            lap_list = LaptopSpec.objects.order_by(order)
            context = {"lap_list": lap_list}
            return render(request, "specs/main.html", context)
        except:
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
    cartID = []
    if request.method == "POST":
        ids = request.POST["ID"]
        cartID.append(ids)
        for id in cartID:
            specs = LaptopSpec.objects.filter(id=id)
            print(specs[0])
        return render(request, "cart.html", {"specs": specs})
    else:
        print("asdfghjgfdsaDFGH")
        return render(request, "cart.html")


#def sort(request):
#    if request.method == "GET":
#        order = request.GET["order"]
#        print(order)
#        lap_list = LaptopSpec.objects.order_by(order)
#        context = {"lap_list": lap_list}
#        return render(request, "specs/main.html", context)
#    else:
#        return Http404("Kutgya?")
