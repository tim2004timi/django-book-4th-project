from django.db import models


class Post(models.Model):
    text = models.TextField()
    objects = models.Manager()

    def __str__(self):
        return self.text[:20]
