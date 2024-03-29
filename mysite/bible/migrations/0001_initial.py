# Generated by Django 4.2.1 on 2023-07-21 06:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=100)),
                ('bible_name', models.CharField(null=True, verbose_name=10)),
                ('author', models.TextField()),
                ('when', models.TextField()),
                ('where', models.TextField()),
                ('whom', models.TextField()),
                ('topic', models.TextField()),
                ('chapter_count', models.IntegerField(null=True)),
                ('chapter_ready', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Testament',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=14)),
            ],
        ),
        migrations.CreateModel(
            name='Verse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('chapter', models.IntegerField(default=1)),
                ('verse', models.IntegerField(default=1)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bible.book')),
                ('testament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bible.testament')),
            ],
            options={
                'ordering': ['chapter', 'verse'],
            },
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.IntegerField(null=True)),
                ('text', models.TextField()),
                ('verse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bible.verse')),
            ],
        ),
        migrations.AddIndex(
            model_name='book',
            index=models.Index(fields=['bible_name'], name='bible_book_bible_n_1e6c51_idx'),
        ),
    ]
