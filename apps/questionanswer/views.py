from django.shortcuts import render,redirect,HttpResponse
from .models import *
from django import views
from .forms import *
from apps.marks.forms import *
from apps.exam.forms import *

class CheckAnswer(views.View):
    def get(self,request,*args, **kwargs):
        if request.user.is_authenticated:
            loggeduser=profiles.objects.get(Username__username=request.user)
            a=Exam.objects.filter(on_project__project_name='Exam  Demo')
            aa = a[0]
            questions =aa.que_of_project.all()

            questions=Questions.objects.all()
            for x in range(0,len(questions)):
                b=questions[x].Questions
                if b.filter(by_user__username=request.user,answered=True):
                    continue
                
                else:
                    c=questions[x].id
                    break

        if 'c' in locals(): #this conditon checks if 'c' is defined or not
            d=Questions.objects.get(id=c)
        else:
            return redirect('profiles:profile')

        return render(
            request,
            'Exam.html',
            context={
                'marksForm':MarksForm(initial={'by_user':loggeduser,'marks_scored':d.Question_weightage}),
                'form':QAForm(initial={'que':d,'by_user':loggeduser}),
                'question':d
            }
        )

    def post(self,request,*args, **kwargs):
        answered_question_id=request.POST['question.id']
        question=Questions.objects.get(id=answered_question_id)
        b=question.correct_answer
        checkedAnswer=request.POST['checkbox']
        
        if b == checkedAnswer:
            Question_form=QAForm(request.POST)
            Marks_form=MarksForm(request.POST)
            if Question_form.is_valid() and Marks_form.is_valid():
                Question_form.save()
                Marks_form.save()
        else :
            print('Wrong ANswer')
            Question_form=QAForm(request.POST)
            Marks_form=MarksForm(request.POST)
            if Question_form.is_valid() and Marks_form.is_valid():
                Question_form.save()
                marks_form = Marks_form.save( commit=False)
                marks_form.marks_scored = 0
                marks_form.save()
       
        

        return redirect('QA:GiveExam')


