from django.shortcuts import render, HttpResponse, redirect
from .models import Verse, Book, Testament
from django.apps import apps
from django.db.models import Max
# Create your views here.


def root(request, pg):
    context = {}
    model = apps.get_model('bible', 'Verse')
    print(model)
    verses = model.objects.filter(chapter=pg).order_by('verse').all()
    book_name = verses[0].book.name
    if not len(verses):
        return redirect(to=f'/bible/{pg-1}')

    if pg < 5:
        next_page = pg + 1
    else:
        next_page = None
    if pg > 1:
        prev_page = pg-1
    else:
        prev_page = None

    print(prev_page, next_page)
    context.update({'verses': verses, 'next_page': next_page, 'prev_page': prev_page, 'book_name': book_name})
    return render(request, 'bible/root.html', context=context)


