# Generated by Django 4.0.1 on 2022-01-31 19:42

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_alter_books_managers'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='books',
            managers=[
                ('active', django.db.models.manager.Manager()),
            ],
        ),
    ]