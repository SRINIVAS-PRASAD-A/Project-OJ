from django.http import HttpResponseRedirect
from django.utils import timezone
from django.shortcuts import render,get_object_or_404


from .models import Problem,Solution
import os,filecmp
# Create your views here.

def problems(request):
    problems_list = Problem.objects.all()
    context = {'problems_list':problems_list}
    return render(request,'judge/index.html',context)

def problemDetail(request,problem_id):
    problem = get_object_or_404(Problem,pk=problem_id)
    return render(request,'judge/detail.html',{'problem':problem})

def submitProblem(request,problem_id):
    
    pass

def leaderboard(request):
    solutions = Solution.objects.all()
    return render(request,'judge/leaderboard.html',{'solutions':solutions})