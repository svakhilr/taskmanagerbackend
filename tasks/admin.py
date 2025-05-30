from django.contrib import admin
from .models import Tasks

class TaskAdmin(admin.ModelAdmin):
    pass

admin.site.register(Tasks,TaskAdmin)
