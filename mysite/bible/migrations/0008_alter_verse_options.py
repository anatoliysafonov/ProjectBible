# Generated by Django 4.2.1 on 2023-06-04 12:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bible', '0007_book_bible_book_bible_n_1e6c51_idx'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='verse',
            options={'ordering': ['id']},
        ),
    ]