from django.shortcuts import render
from .models import FaqL
from django.contrib import messages

# Create your views here.
def home(request):
    if request.method == "GET":
        faq = FaqL.objects.order_by("id").exclude(answer='')
        content = {"faq": faq}
        return render(request, "faq_home.html",content)
    else:
        Q = request.POST["Question"]
        A = request.POST["Author"]
        F = FaqL.objects.create(question=Q,author=A)
        F.save()
        messages.success(request, 'Question Successfully added!')
        faq = FaqL.objects.order_by("id").exclude(answer='')
        content = {"faq": faq}
        return render(request,"faq_home.html",content)