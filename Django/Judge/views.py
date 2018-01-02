from django.shortcuts import render, redirect
from .models import Problem, Submit, User


def user(request, uid):
    context = {
        'user': User.objects.get(id=uid),
        'submit': Submit.objects.filter(user=User.objects.get(id=uid)),
        'n_submit': Submit.objects.filter(user=User.objects.get(id=uid)).count(),
        'n_AC': Submit.objects.filter(user=User.objects.get(id=uid)).filter(status=True).count(),
        'n_WA': Submit.objects.filter(user=User.objects.get(id=uid)).filter(status=False).count(),
    }
    return render(request, 'user.html', context)


def problem_list(request):
    context = {
        'problems': Problem.objects.all(),
    }

    return render(request, 'problem_list.html', context)


def problem(request, pid):
    context = {
        'problem': Problem.objects.get(id=pid)
    }
    return render(request, 'problem.html', context)


def status(request):
    context = {
        'submits': Submit.objects.order_by('-time'),
    }
    return render(request, 'status.html', context)


def submit(request, pid):
    context = {
        'problem': Problem.objects.get(id=pid)
    }
    return render(request, 'submit.html', context)


def submitted(request, pid):
    if request.POST:
        Submit.objects.create(
            user=request.user,
            problem=Problem.objects.get(id=pid),
            code=request.POST.get('code'),

        )
    return redirect('/status/')
