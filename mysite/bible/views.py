from django.shortcuts import render, redirect
from .models import Verse
from django.core.cache import cache
from django.apps import apps
from copy import copy
import pickle
# Create your views here.


def make_text_linked(verses: list):
    import re
    LINK_HREF = "<a class='text-sup' href='/bible/primitku/#{}'><sup><b>{}</b></sup></a>"
    linked_verses = copy(verses)
    testament = linked_verses[0].testament.id
    book = linked_verses[0].book.id
    for verse in linked_verses:
        tags = re.findall(r'<[а-я\d]*>', verse.text)
        for tag in tags:
            tag_shorted = tag[1:-1]
            href = '-'.join([str(testament), str(book), tag_shorted])
            verse.text = verse.text.replace(tag, LINK_HREF.format(href, tag_shorted))
    return linked_verses


def index(request, book: int, chapter: int):
    cached_book = cache.get('book_text')
    if cached_book:
        book_query = pickle.loads(cached_book)
    else:
        book_query = Verse.objects.all()
        cache.set('book_text', pickle.dumps(book_query))
    verses = book_query.filter(book=book).filter(chapter=chapter).all()
    book_name = verses[0].book.name
    next_page = chapter + 1 if chapter < 5 else None
    prev_page = chapter - 1 if chapter > 1 else None
    verses = make_text_linked(verses)
    context = {'verses': verses,
               'next_page': next_page,
               'prev_page': prev_page,
               'book_name': book_name,
               'book': book,
               }
    return render(request, 'bible/root.html', context=context)


# Create your views here

def page404(request):
    return render(request, 'bible/404.html',  {})
