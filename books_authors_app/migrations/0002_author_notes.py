# Generated by Django 2.2 on 2021-05-11 05:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('books_authors_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='notes',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
