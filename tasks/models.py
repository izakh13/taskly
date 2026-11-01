from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    class Status(models.TextChoices):
        NEW = ("new", "New")
        IN_PROGRESS = ("in_progress", "In Progress")
        DONE = ("done", "Done")

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=Status, default=Status.NEW)
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')

    def __str__(self):
        return f'{self.title} ({self.created_at.strftime('%d.%m.%Y %H:%M')})'
