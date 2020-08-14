from django.shortcuts import render


def home(request):
    return render(request,"Home/index.html")
# Create your views here.
def laptop(request):
    return render(request,"specs/main.html")