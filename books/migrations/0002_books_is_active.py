# Generated by Django 4.0.1 on 2022-01-31 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='is_active',
            field=models.CharField(default='Y', max_length=1),
        ),
    ]
