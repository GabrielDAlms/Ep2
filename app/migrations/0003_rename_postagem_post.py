# Generated by Django 4.2.7 on 2023-11-15 01:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_category'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Postagem',
            new_name='Post',
        ),
    ]
