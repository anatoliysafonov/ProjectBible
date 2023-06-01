import pickle

from django.shortcuts import render
from django.core.cache import cache

from .models import Verse, Book
from .sevices import make_text_linked


def index(request, book: int, chapter: int):
    verses_to_page = []
    verses = cache.get('verses') if (cache.get('book') == book) else None
    if not verses:
        verses = Verse.objects.filter(book=book).all()
        cache.set('verses', pickle.dumps(verses))
        cache.set('book', book)
    else:
        verses = pickle.loads(verses)
    for verse in verses:
        if verse.chapter == chapter:
            verses_to_page.append(verse)
    book_name = cache.get('book_name')
    if not book_name:
        book_name = Book.objects.filter(id=book).get().name # noqa
        cache.set('book_name', book_name)
    next_page = chapter + 1 if chapter < 5 else None
    prev_page = chapter - 1 if chapter > 1 else None
    verses = make_text_linked(verses=verses_to_page)
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
