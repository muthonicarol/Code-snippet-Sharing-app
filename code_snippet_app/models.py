from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Snippet (models.Model):
    language = models.CharField(max_length= 50)
    description = models.CharField(max_length=100)
    code = models.TextField()
    created_by = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.language + '' + self.description



