from django.contrib import admin

# Register your models here.
from judge.models import Problem,Testcases,Solution

admin.site.register(Problem)
admin.site.register(Testcases)
admin.site.register(Solution)