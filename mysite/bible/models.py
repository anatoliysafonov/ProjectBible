from django.db import models
from django.db.models import ForeignKey, IntegerField, TextField, CASCADE
# Create your models here.


class Book(models.Model):
    name = TextField(max_length=100)
    author = TextField()
    when = TextField()
    where = TextField()
    whom = TextField()
    topic = TextField()
    chapter_count = IntegerField(null=True)


class Testament(models.Model):
    name = TextField(max_length=14)


class Verse(models.Model):
    text = TextField()
    chapter = IntegerField(null=False, default=1)
    verse = IntegerField(null=False, default=1)
    testament = ForeignKey(Testament, on_delete=CASCADE)
    book = ForeignKey(Book, on_delete=CASCADE)

    class Meta:
        ordering = ['verse']