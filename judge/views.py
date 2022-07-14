from django.http import HttpResponseRedirect
from django.utils import timezone
from django.urls import reverse
from django.shortcuts import render,get_object_or_404


from .models import Problem,Solution,Testcases
import subprocess,filecmp
# Create your views here.

def problems(request):
    problems_list = Problem.objects.all()
    context = {'problems_list':problems_list}
    return render(request,'judge/index.html',context)

def problemDetail(request,problem_id):
    problem = get_object_or_404(Problem,pk=problem_id)
    return render(request,'judge/detail.html',{'problem':problem})

def submitProblem(request,problem_id):
    if('solution' in request.FILES):
        f = request.FILES['solution']
        with open("D:\Project-OJ\solution.cpp",'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)
    elif('solution' in request.POST):
        code = request.POST['solution']
        f = open("D:\Project-OJ\solution.cpp",'w+')
        f.write(code)
        f.close()

    #testcase = Testcases()
    testcase = Testcases.objects.get(problem=problem_id)
    #testcase.problem = Problem.objects.get(pk = problem_id)
    compile = r"g++ D:\Project-OJ\solution.cpp -o D:\Project-OJ\solution"
    run = r"D:\Project-OJ\solution <"+"\"" +testcase.input + "\""+ r">D:\Project-OJ\output.txt"
    s = subprocess.check_call(compile,shell=True)
    s = subprocess.check_call(run,shell=True)
    
    if(filecmp.cmp(r"D:\Project-OJ\output.txt",testcase.output,shallow=True)):
        verdict = 'Accepted'
    else:
        verdict = 'Wrong answer'

    solution = Solution()
    solution.problem = Problem.objects.get(pk = problem_id)
    solution.verdict = verdict
    solution.submitted_at = timezone.now()
    solution.submitted_code = r"D:\Project-OJ\solution.cpp"
    solution.save()
    return HttpResponseRedirect(reverse('judge:leaderboard'))
    

def leaderboard(request):
    solutions = Solution.objects.all()
    return render(request,'judge/leaderboard.html',{'solutions':solutions})