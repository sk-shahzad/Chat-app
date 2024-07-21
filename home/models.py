from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE


class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    content = models.TextField()
    updated = models.DateTimeField(auto_now=True, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering =  ['-updated', '-created']

    def __str__(self):
        return f"Message from {self.sender}"




