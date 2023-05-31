from django.shortcuts import render, redirect
from django.apps import apps


# Create your views here
def root(request, chapter: int):
    model = apps.get_model('bible', 'Verse')
    verses = model.objects.filter(chapter=chapter).order_by('verse').all()
    book_name = verses[0].book.name
    if not len(verses):
        return redirect(to=f'/bible/{chapter-1}')
    next_page = chapter + 1 if chapter < 5 else None
    prev_page = chapter - 1 if chapter > 1 else None
    context = {'verses': verses,
               'next_page': next_page,
               'prev_page': prev_page,
               'book_name': book_name}
    return render(request, 'bible/root.html', context=context)


