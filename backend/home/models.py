from django.db import models
from django.contrib.auth.models import User
# Create your models here.

CHOICES = (
    ("NOVEL","NOVEL"),
    ("DRAMA","DRAMA"),
    ("STORY","STORY"),
    ("FICTION","FICTION"),
    ("MOTIVATIONAL","MOTIVATIONAL"),
)

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=100,choices=CHOICES)
    image = models.FileField(upload_to='movie')
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return f'user :{self.user.username} book:{self.title} auto:{self.author}'















