# Generated by Django 4.0.1 on 2022-01-31 17:48

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_books_is_active'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='books',
            managers=[
                ('Select', django.db.models.manager.Manager()),
            ],
        ),
    ]
