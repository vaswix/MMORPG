from django.contrib.auth.models import User
from django.db import models


class OneTimeCode(models.Model):
    code = models.SmallIntegerField()
    email = models.EmailField()
