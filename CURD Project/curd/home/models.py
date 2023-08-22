from django.db import models

# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length=50,null=False)
    email=models.EmailField(max_length=50,null=False)
    password=models.CharField(max_length=50,null=True)

    def __str__(self):
        return self.name

