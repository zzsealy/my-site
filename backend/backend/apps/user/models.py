from django.db import models
# Create your models here.

# Create your models here.


class User(models.Model):
    id = models.IntegerField(primary_key=True)
    phone_number = models.CharField('手机号', max_length=11, blank=True)
    username = models.CharField(help_text='用户名', max_length=100)
    password = models.CharField(help_text='密码', max_length=100)
    email = models.EmailField(help_text='邮箱', blank=True)

    class Meta:
        db_table = "user"