from multiprocessing import context
from django.shortcuts import render, HttpResponse, redirect
import random

def index(request):
    request.session['great_num'] = random.randint(1, 100)
    print(request.session['great_num'])
    return render(request, 'index.html')

def guessing(request):
    num = int(request.POST['num'])
    def checking():
        if num == request.session['great_num']:
            return 0
        elif num < request.session['great_num']:
            return 1
        else:
            return 2
    context = {
        "afterCheck": int(checking())
    }
    return render(request, "index.html", context)
