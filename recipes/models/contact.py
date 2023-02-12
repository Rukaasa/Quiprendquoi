from django.db import models


class Students(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField(max_length=40)
    section = models.CharField(max_length=25)

    def __str__(self):
        return self.name
