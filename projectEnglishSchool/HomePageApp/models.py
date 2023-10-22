from django.db import models
from datetime import datetime
from django.urls import reverse

class DatePerson(models.Model):
    name = models.CharField(max_length=20, blank=False)
    second_name = models.CharField(max_length=35)
    age = models.IntegerField(default=0)
    numberPhon = models.TextField(max_length = 10, blank=False)
    date = models.DateTimeField(default= datetime.now())

    def __str__(self):
        return f'{self.name} {self.second_name}'

    def get_absolute_url(self):
        return reverse('post-datail', args= str(self))
