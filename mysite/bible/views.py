from django.shortcuts import render, HttpResponse
from .models import Verse, Book, Testament
# Create your views here.


def root(requesst):
    resp = 'Non ce'
    verses = Verse.objects.filter(chapter=5).all()
    count = verses[0].book.chapter_count
    print(count)
    if verses:
        resp = ''
        for vers in verses:
            resp = resp + f'<h3>{vers.text}</h3>'
    return HttpResponse(resp)

