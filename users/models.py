from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=50)
    headimg = models.FileField(upload_to="img/")

    def __str__(self):
        return self.name
