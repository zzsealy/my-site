# Generated by Django 3.2.8 on 2021-11-18 06:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Images',
            new_name='Image',
        ),
        migrations.RemoveField(
            model_name='article',
            name='image',
        ),
    ]
