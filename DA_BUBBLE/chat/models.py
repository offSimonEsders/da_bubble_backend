from django.db import models
from account.models import DA_Bubble_User

from datetime import datetime

class Message(models.Model):
    author = models.ForeignKey(DA_Bubble_User, on_delete=models.CASCADE)
    created_at = models.DateField(default=datetime.today())
    message = models.TextField()
    
class Reaction(models.Model):
    author = models.ForeignKey(DA_Bubble_User, on_delete=models.CASCADE)
    created_at = models.DateField(default=datetime.today())
    reaction = models.CharField(max_length=1)
    on_message = models.ForeignKey(Message, on_delete=models.CASCADE)