from django.contrib import admin

from .models import ProjectModel, NoteModel

admin.site.register(ProjectModel)
admin.site.register(NoteModel)
