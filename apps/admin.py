from django.contrib import admin
from apps.models import *
for m in (Picture, Tag, Idea, Collaborator, App):
    admin.site.register(m)