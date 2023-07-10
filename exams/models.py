from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    pass


class Question(models.Model):
    text = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.text


class Test(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    test_num = models.CharField(max_length=15)
    results = models.IntegerField()
