from django.contrib import admin
from apps.profiles.models import *
# Register your models here.
class profilesadmin(admin.ModelAdmin):
    list_display = ('Username','user_type','profile_created_on','modified_on')

admin.site.register(profiles,profilesadmin)
