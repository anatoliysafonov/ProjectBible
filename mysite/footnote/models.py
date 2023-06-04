from django.db import models
from django.db.models import TextField, CharField

# Create your models here.


class Footnote(models.Model):
    code = CharField(10, unique=True)
    text = TextField()

    def __str__(self):
        return self.text

    class Meta:
        ordering = ['id']
        indexes = [
            models.Index(fields=['code'])
        ]
