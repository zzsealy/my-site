from django.db import models
from django.core.validators import MinLengthValidator

from django.contrib.auth.models import AbstractUser
# Create your models here.

# Create your models here.


class User(AbstractUser):
    phonenumber = models.CharField('手机号', max_length=11, 
                                   validators=[MinLengthValidator(11)], blank=True)
