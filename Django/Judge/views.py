from django.shortcuts import render
from .models import Problem, Submit


def user(request):
    context = {
        'user': request.user,
        'submit': Submit.objects.get(user=request.user)
    }
    return render(request, 'user.html', context)


def problem_list(request):
    context = {
        'problems': Problem.objects.all(),
    }

    return render(request, 'problem_list.html', context)


def problem(request, pid):
    pass


def status(request):
    pass
