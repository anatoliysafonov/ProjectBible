from django.shortcuts import render, HttpResponse

from .models import Footnote


# Create your views here.


def root(request, code: str):
    print(code)
    text = Footnote.objects.filter(code=code).get()
    return HttpResponse(f"<p>{text}</p>")