from django.db import models

# Create your models here.

class ride(models.Model):
    DIFFICULTY = (
        ('Easy', '1'),
        ('Medium', '2'),
        ('Hard', '3'),
        ('Very Hard', '4'),
        ('Nightmare', '5')
    )
    title = models.CharField(max_length=100)
    length = models.IntegerField()
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY)
    description = models.CharField(max_length=999)


#class user(models.Model):
    #username = models.CharField(max_length=16)
    #





#class comment(models.Model)
    #
