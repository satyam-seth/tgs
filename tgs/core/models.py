from django.db import models

# Create your models here.

class Winner(models.Model):
    team_logo=models.ImageField(upload_to="home/",default='Not Available')
    team_name=models.CharField(max_length=50,default='Not Available')

    def __str__(self):
        return self.team_name