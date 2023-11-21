import os

from django.db import models
from django.contrib.auth.models import User

from organisation.models import Organisation


class TaskDesk(models.Model):
    create_user = models.ForeignKey(User, on_delete=models.CASCADE)
    organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    creation_timestamp = models.DateTimeField(auto_now_add=True)


class Task(models.Model):
    create_user = models.ForeignKey(User, on_delete=models.CASCADE)
    task_id = models.CharField(max_length=12)
    head_text = models.TextField()
    mid_text = models.TextField()
    task_desk = models.ForeignKey(TaskDesk, on_delete=models.CASCADE)
    creation_timestamp = models.DateTimeField(auto_now_add=True)


class HeadTextFile(models.Model):
    create_user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='temp')
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    creation_timestamp = models.DateTimeField(auto_now_add=True)

    def delete(self, *args, **kwargs):
        if self.file:
            file_path = self.file.path
            if os.path.exists(file_path):
                os.remove(file_path)
        super().delete(*args, **kwargs)


class MidTextFile(models.Model):
    create_user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='temp')
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    creation_timestamp = models.DateTimeField(auto_now_add=True)

    def delete(self, *args, **kwargs):
        if self.file:
            file_path = self.file.path
            if os.path.exists(file_path):
                os.remove(file_path)
        super().delete(*args, **kwargs)


class Commentary(models.Model):
    create_user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    text = models.TextField(null=True, blank=True)
    creation_timestamp = models.DateTimeField(auto_now_add=True)


class CommentaryFile(models.Model):
    commentary = models.ForeignKey(Commentary, on_delete=models.CASCADE)
    file = models.FileField(upload_to='temp')
    creation_timestamp = models.DateTimeField(auto_now_add=True)

    def delete(self, *args, **kwargs):
        if self.file:
            file_path = self.file.path
            if os.path.exists(file_path):
                os.remove(file_path)
        super().delete(*args, **kwargs)
