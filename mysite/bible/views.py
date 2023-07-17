import pickle
from django.shortcuts import render
from django.core.cache import cache
from django.http import JsonResponse
from .models import Verse, Book, Note 
from .sevices import make_text_linked


def index(request, book: str='matt', chapter: int=1):
    user = request.user.id if request.user.id else 0
    print('USER:', user)
    # список віршів для виводу на сторінку
    verses_to_page = []
    # Завантажуємо вірші з redis. Якщо помінялась книга, то вірші будуть завантажені з нової книги
    verses = cache.get('verses') if (cache.get('book') == book) else None
    # завантажуємо дані книги з redis.
    book_data = cache.get('book_data')
    # якщо даних книги немає, то завантажуємо і кешуємо дані
    if not book_data:
        book_data = Book.objects.filter(bible_name=book).get()  # noqa
        cache.set('book_data', pickle.dumps(book_data))
    else:
        book_data = pickle.loads(book_data)
    # якщо кешованих віршів немає, то завантажуємо і кешуємо їх
    if not verses:
        verses = Verse.objects.filter(book=book_data.id).all()
        cache.set('verses', pickle.dumps(verses))
        # кешуємо назву книги
        cache.set('book', book)
    else:
        verses = pickle.loads(verses)
    # готуємо список віршів дял виведення
    for verse in verses:
        if verse.chapter == chapter:
            verses_to_page.append(verse)
    next_page = chapter + 1 if chapter < book_data.chapter_ready else None
    prev_page = chapter - 1 if chapter > 1 else None

    verses = make_text_linked(verses=verses_to_page)
    context = {'verses': verses,
               'next_page': next_page,
               'prev_page': prev_page,
               'book_name': book_data.name,
               'book': book,
               }
    return render(request, 'bible/verses.html', context=context)


# Create your views here

def page404(request):
    return render(request, 'bible/404.html',  {})


def ajaxreadnote(request):
    answer = 'поки без коментара'
    uuid = 0
    if request.method == "POST":
        data = request.POST.get('uuid')
        note_text = Note.objects.filter(code=str(data))
        if note_text:
            answer = note_text[0].text
    return JsonResponse({'result': answer, 'uuid': data}, status=200)

def ajaxwritenote(request):
    if request.method == "POST":
        text = request.POST.get('text')
        uuid = request.POST.get('uuid')
        note = Note.objects.filter(code=uuid).first()
        if not note:
            note = Note(code=uuid, text=text)

        else:
            note.text = text
        note.save()
        
        
    return JsonResponse({'result': text}, status=200)