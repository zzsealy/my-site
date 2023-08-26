# Generated by Django 3.2.8 on 2023-08-25 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('password', models.CharField(help_text='密码', max_length=100)),
                ('email', models.CharField(help_text='邮箱', max_length=100)),
                ('nick_name', models.CharField(help_text='昵称', max_length=20)),
            ],
            options={
                'db_table': 'user',
            },
        ),
        migrations.CreateModel(
            name='UserEmailVerCode',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('user_id', models.IntegerField(db_index=True, help_text='user表的id')),
                ('ver_code', models.CharField(help_text='验证码', max_length=6)),
                ('expire_datetime', models.DateTimeField()),
            ],
            options={
                'db_table': 'user_email_ver_code',
            },
        ),
    ]
