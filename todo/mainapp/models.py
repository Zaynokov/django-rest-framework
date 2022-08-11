from django.db import models

from userapp.models import UserModel


class ProjectModel(models.Model):

    name = models.CharField(
        max_length=64)

    repository = models.URLField(
        blank=True)

    users = models.ManyToManyField(
        UserModel)

    def __str__(self):
        return self.name


class NoteModel(models.Model):

    project = models.ForeignKey(
        ProjectModel,
        on_delete=models.CASCADE)

    body = models.TextField(
        max_length=500)

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE)

    created_at = models.DateTimeField(
        auto_now_add=True)

    updated_at = models.DateTimeField(
        auto_now=True)

    is_active = models.BooleanField(
        default=True)
