from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
# Create your models here.

class profiles(models.Model):
    class Meta:
        verbose_name_plural='Profile\'s'
    
    Username=models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        unique=True,
        related_name='profile',
    )
    first_name=models.CharField(
        max_length=25,
    )
    last_name=models.CharField(
        max_length=25,
    )
    email_id=models.EmailField()

    profile_dp=models.ImageField(
        verbose_name='Profile Picture',
        upload_to = 'static/images',
        
        default='static/images/tenor.gif'
    )    

    profile_created_on=models.DateTimeField(
        auto_now_add=True,
    )
    
    modified_on=models.DateTimeField(
        auto_now=True,
    )

    experience=models.IntegerField(
        null=True,
    ) #which field is appropriate for experience

    previous_projects=models.TextField(
        null=True,
        blank=True,
    )

    Area_of_Interest=models.CharField(
        max_length=200,
        default='Python'
    )

    city=models.TextField(default='Batala Road,Amritsar,India')

    Something_about_yourself=models.TextField(default='NA')

    user_type=models.CharField(
        max_length=2,
        choices=(
            ('D','Developer'),
            ('R','Recruiter'),
            ('B','Both'),
            ),
       verbose_name='Type of profile',
       default='D',
    )

def create_profile(sender,**kwargs ):
    print(kwargs)
    if kwargs['created']:
        user_profile=profiles.objects.create(Username=kwargs['instance'])


post_save.connect(create_profile,sender=User)