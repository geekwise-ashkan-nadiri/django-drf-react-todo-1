from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=20)
    desc = models.TextField()
    complete = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title}"