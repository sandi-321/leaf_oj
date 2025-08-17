from django.shortcuts import render, redirect, get_object_or_404
from .models import Problem
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .models import *

# Create your views here.
def index_view(request):
    return render(request, 'leaf_oj/index.html')

def problems_view(request):
    problems = Problem.objects.order_by("problem_id")
    return render(request, "leaf_oj/problems.html",{"problems": problems})

def problem_view(request, problem_id):
    problem = get_object_or_404(Problem, problem_id=problem_id)
    context = {
        "problem": problem,
    }
    return render(request, 'leaf_oj/problem.html', context)

def login_view(request):
    if request.user.is_authenticated:
        return redirect('leaf_oj:index')
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                
                next_url = request.POST.get('next', '') or request.GET.get('next', '')
                return redirect(next_url) if next_url else redirect('leaf_oj:index')
    else:
        form = AuthenticationForm()
        next_url = request.GET.get('next', '')

    return render(request, 'leaf_oj/login.html', {'form': form,})