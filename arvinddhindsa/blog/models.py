from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
# migrate makemigrations


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)     #no () because we dont want to execute the function
    author = models.ForeignKey(User, on_delete=models.CASCADE)   #A user can have many posts, but a post cannot have multiple users

    def __str__(self):
        return self.title



