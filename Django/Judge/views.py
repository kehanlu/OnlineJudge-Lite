from django.shortcuts import render, redirect
from .models import Problem, Submit, User
import docker
import threading
import time

class Compile(object):
    def __init__(self, submit, problem):
        self.cid = str(submit.id)
        self.problem = problem
        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True
        thread.start()

    def run(self):
        client = docker.APIClient(base_url='unix://var/run/docker.sock')
        compile_cmd = "g++ /home/jail/" + self.cid + ".cpp -o /home/jail/" + self.cid + ".o -fno-asm -O2 -Wall -lm --static -DONLINE_JUDGE"
        compile_exec = client.exec_create(container = "oj_sandbox", cmd = compile_cmd)

        if self.problem.test_input == '':
            execute_cmd = "/home/jail/"+self.cid+".o";
        else:
            execute_cmd = "/home/jail/"+self.cid+".o < /home/jail/"+self.cid+".testdata";

        print(execute_cmd)

        print(client.exec_start(compile_exec["Id"]))
        
        execute_exec = client.exec_create(container = "oj_sandbox",user = "jail", cmd = "sh -c \"" + execute_cmd + "\"")
        result = client.exec_start(execute_exec["Id"]).decode("utf-8")
        
        result = result.strip(' \t\n\r').replace("\r\n", "\n")
        test_ouput = self.problem.test_ouput.strip(' \t\n\r').replace("\r\n", "\n")

        if result == test_ouput:
            Submit.objects.filter(id=int(self.cid)).update(status=True)
        else:
            Submit.objects.filter(id=int(self.cid)).update(status=False)
        
        self._running = False

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
        problem = Problem.objects.get(id=pid)
        submit = Submit.objects.create(
            user=request.user,
            problem=problem,
            code=request.POST.get('code'),
        )
        file = open("/tmp/oj/"+str(submit.id)+".cpp", 'w')
        file.write(request.POST.get('code'))
        file.close()

        if problem.test_input != '':
            file = open("/tmp/oj/"+str(submit.id)+".testdata", 'w')
            file.write(problem.test_input)
            file.close()

        compileTask = Compile(submit, problem)
        
        
    return redirect('/status/')
