from django.db import models

# Create your models here.

class Daily(models.Model):
    date=models.DateField()
    match_type=models.CharField(max_length=5)
    fees=models.DecimalField(decimal_places=2,max_digits=7)
    total_games=models.IntegerField()

    def __str__(self):
        return str(self.date)+' '+self.match_type

class Weekly(models.Model):
    date=models.DateField()
    match_type=models.CharField(max_length=5)
    fees=models.DecimalField(decimal_places=2,max_digits=7)
    total_games=models.IntegerField()

    def __str__(self):
        return str(self.date)+' '+self.match_type

class Monthly(models.Model):
    date=models.DateField()
    match_type=models.CharField(max_length=5)
    fees=models.DecimalField(decimal_places=2,max_digits=7)
    total_games=models.IntegerField()

    def __str__(self):
        return str(self.date)+' '+self.match_type

class Djoin(models.Model):
    date=models.DateField()
    time=models.TimeField()
    cid=models.IntegerField()
    team_name=models.CharField(max_length=50)
    leader_pname=models.CharField(max_length=50)
    second_pname=models.CharField(max_length=50)
    third_pname=models.CharField(max_length=50)
    fourth_pname=models.CharField(max_length=50)
    fifth_pname=models.CharField(max_length=50)
    whats_num=models.IntegerField()
    pay_ss=models.ImageField(upload_to="djoin/pss/")
    team_logo=models.ImageField(upload_to="djoin/logo/",default='Not Available')

    def __str__(self):
        return str(self.cid)+' '+self.team_name