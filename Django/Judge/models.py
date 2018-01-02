from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    n_submit = models.IntegerField(default=0)
    n_AC = models.IntegerField(default=0)
    n_WA = models.IntegerField(default=0)


class Problem(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    description = models.TextField(blank=True)
    test_input = models.TextField(blank=True)
    test_ouput = models.TextField(blank=True)
    hint = models.TextField(blank=True)
    time = models.CharField(max_length=200, blank=True)
    memory = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name


class Submit(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='submit')
    problem = models.ForeignKey(
        Problem, on_delete=models.CASCADE, related_name='submit')
    status = models.NullBooleanField(blank=True, null=True)

    def __str__(self):
        s = 'X'
        if self.status:
            s = 'O'
        return "{} === {} : {}".format(s, self.user, self.problem)
