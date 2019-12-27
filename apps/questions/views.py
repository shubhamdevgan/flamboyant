from django.shortcuts import render
from django import views
import random
from .models import *
from django.core.paginator import Paginator
import random

def DisplayQuestion(request):
    question_ids = []
    for x in Questions.objects.all():
        question_ids.append(x.id)

    asked_questions_id = []

    id_to_be_asked=random.choice(question_ids)

    if id_to_be_asked not in asked_questions_id:
        final_question=Questions.objects.get(id=id_to_be_asked)
        asked_questions_id.append(id_to_be_asked)
        
    print(asked_questions_id)
    return render(
        request,
        'Exam.html',
        context={
            'form':final_question
        }
    )
