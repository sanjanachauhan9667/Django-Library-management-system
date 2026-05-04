from django.db import models

# Create your models here.

class LibraryHub(models.Model):

    Status_Choices = [
        ('available','Available'),
        ('issued','Issued'),
    ]

    name = models.CharField(max_length=50)
    author = models.CharField(max_length=100)
    status = models.CharField(max_length=100, choices= Status_Choices)

    def __str__(self):
        return self.name
