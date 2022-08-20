from django.db import models

# Create your models here.
class activity(models.Model):
    DIFFICULTY = (
        ('Easy', '1'),
        ('Medium', '2'),
        ('Hard', '3'),
        ('Very Hard', '4'),
        ('Nightmare', '5')
    )
    TYPE = (
        ('Road Bike', 'RB'),
        ('Mountain Bike', 'MB'),
        ('Hike', 'H')
    )
    title = models.CharField(max_length=100)
    type = models.CharField(max_length=10, choices=TYPE)
    length = models.IntegerField()
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY)
    description = models.CharField(max_length=999, default='')








#class user(models.Model):
    #username = models.CharField(max_length=16)
    #





#class comment(models.Model)
    #
