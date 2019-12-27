from django.db import models
from apps.exam.models import *
from apps.exam.models import *
class Questions(models.Model):

    of_project=models.ForeignKey(
        Exam,
        on_delete=models.CASCADE,
        related_name='que_of_project',
        null=True,
        blank=True

    )
    question_text=models.CharField(
        max_length=150,
    )

    option_1=models.CharField(
        max_length=50
    )

    option_2=models.CharField(
        max_length=50
    )

    option_3=models.CharField(
        max_length=50
    )

    option_4=models.CharField(
        max_length=50
    )


    correct_answer=models.CharField(
        max_length=2,
        choices=(('01','option_1'),
        ('02','option_2'),
        ('03','option_3'),
        ('04','option_4'),
        )
    )

    Question_weightage=models.IntegerField(
        verbose_name='Enter Weightage for Question',
        help_text='Weightage should be marks to given for Correct Answer')

    def __str__(self):
        return self.question_text