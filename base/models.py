from django.db import models

status_list = [('Done','Done'),('Inprogress','Inprogress'),('Incomplete','Incomplete')]

# Create your models here.
class ToDo(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    status = models.CharField(max_length=30 , choices=status_list)

    def __str__(self):
        return self.name

