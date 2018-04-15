from django.db import models

# Create your models here.


class Post(models.Model):
    text = models.TextField()

    def __str__(self):
        "A string repr of django model"
        return self.text[:30]
