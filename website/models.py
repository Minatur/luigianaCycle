from django.db import models

# Create your models here.

class ride(models.Model):
    DIFFICULTY = (
        ('1', 'Easy')
        ('2', 'Medium')
        ('3', 'Hard')
        ('4', 'Very Hard')
        ('5', 'Nightmare')
    )
    title = models.CharField(max_length=100)
    length = models.IntegerField()
    difficulty = models.CharField(max_length=1, choices=DIFFICULTY)


#class user(models.Model):






#class comment(models.Model)
