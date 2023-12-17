from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField( max_length=50)
    details = models.TextField()
    
    def __str__(self):
        return self.title
    
