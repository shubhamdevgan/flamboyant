from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
class projects(models.Model):
    class Meta:
        verbose_name_plural='Projects\'s'
    
    by_username=models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='projects',
    )
    
    project_name=models.CharField(
        max_length=150,
        verbose_name="Project Name",

    )

    status=models.CharField(
        max_length=3,
        choices=(
            ('PEN','PENDING'),
            ('CAN','CANCELLED'),
            ('COM','COMPLETED'),
            ('ACC','ACCEPTED')
        ),

        default='PEN'
    )

    has_exam=models.CharField(
        max_length=2,
        choices=(
            ('NO','NO'),
            ('YS','YES'),
        ),

        default='NO'
    )

    project_details=models.TextField(
        verbose_name='Complete Decription about Project',
    )

    skills=models.CharField(
        max_length=10,
    )

    budget=models.TextField(
        verbose_name='Enter your budget',
    )

    time_frame=models.TextField(
        verbose_name='Required Working Hours'
    )

    def __str__(self):
        return self.project_name
        
def link_profile(sender,**kwargs):
    print(kwargs)

post_save.connect(link_profile,sender=projects)
