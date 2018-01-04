from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    n_submit = models.IntegerField(default=0)
    n_AC = models.IntegerField(default=0)
    n_WA = models.IntegerField(default=0)
    school = models.CharField(max_length=200)


class Problem(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    description = models.TextField(blank=True)
    sample_input = models.TextField(blank=True)
    sample_output = models.TextField(blank=True)
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
    code = models.TextField()
    status = models.NullBooleanField(blank=True, null=True)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        
        if self.status == None:
            s = 'CP'
        elif self.status:
            s = 'AC'
        else:
            s = 'WA'
        return "{} === {} : {}".format(s, self.user, self.problem)
