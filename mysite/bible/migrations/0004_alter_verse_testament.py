# Generated by Django 4.2.1 on 2023-06-01 12:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bible', '0003_alter_verse_testament'),
    ]

    operations = [
        migrations.AlterField(
            model_name='verse',
            name='testament',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bible.testament'),
        ),
    ]