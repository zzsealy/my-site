# Generated by Django 3.2.8 on 2021-11-18 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20211118_0651'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='index',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
