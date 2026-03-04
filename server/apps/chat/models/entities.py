from django.db import models
from django.contrib.auth.models import User

class Chats(models.Model):
    Username = models.ForeignKey(User, on_delete=models.CASCADE)
    Conversations = models.TextField()
    Created_Date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.Username.first_name