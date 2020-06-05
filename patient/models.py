from django.db import models

Condition = [
    ('b', 'Bad'),
    ('g', 'Good')
]


# Create your models here.


class patient(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    gender = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    mobile = models.CharField(max_length=12)
    condition = models.CharField(max_length=1, choices=Condition)
    status = models.BooleanField()



