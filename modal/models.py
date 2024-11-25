from django.db import models

class Person(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()

    def __str__(self):
        
        return self.name

