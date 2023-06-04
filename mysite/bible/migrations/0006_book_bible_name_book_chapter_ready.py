# Generated by Django 4.2.1 on 2023-06-04 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bible', '0005_alter_verse_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='bible_name',
            field=models.CharField(null=True, verbose_name=10),
        ),
        migrations.AddField(
            model_name='book',
            name='chapter_ready',
            field=models.IntegerField(null=True),
        ),
    ]
