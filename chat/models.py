from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class Room(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=1000)

class Message(models.Model):
    id = models.AutoField(primary_key=True)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"From {self.sender} to {self.receiver}"