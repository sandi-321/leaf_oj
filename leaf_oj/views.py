from django.shortcuts import render, redirect, get_object_or_404
from .models import Problem
from .models import *

# Create your views here.
def index(request):
    return render(request, 'leaf_oj/index.html')

def problems(request):
    problems = Problem.objects.order_by("problem_id")
    return render(request, "leaf_oj/problems.html",{"problems": problems})

def problem(request, problem_id):
    problem = get_object_or_404(Problem, problem_id=problem_id)
    context = {
        "problem": problem,
    }
    return render(request, 'leaf_oj/problem.html', context)