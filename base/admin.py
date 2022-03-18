from django.contrib import admin
from .models import projectData, skill, tag, Message, Endorsement, Comment

# Register your models here.

admin.site.register(projectData)
admin.site.register(skill)
admin.site.register(tag)
admin.site.register(Message)
admin.site.register(Endorsement)
admin.site.register(Comment)
