from django.urls import path
from . import views

app_name = 'judge'
urlpatterns = [
    path('',views.problems,name='problems'),
    path('problem/<int:problem_id/',views.problemDetail,name='problem_detail'),
    path('problem/<int:problem_id/submit/',views.submitProblem,name='submit'),
    path('leaderboard',views.leaderboard,name='leaderboard'),
]