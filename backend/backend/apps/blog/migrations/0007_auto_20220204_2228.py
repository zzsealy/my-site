# Generated by Django 3.2.8 on 2022-02-04 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20220120_1558'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='index',
        ),
        migrations.RemoveField(
            model_name='image',
            name='owner_article',
        ),
        migrations.RemoveField(
            model_name='image',
            name='title',
        ),
        migrations.AddField(
            model_name='image',
            name='link',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
