from django.db import models
from django.core.validators import RegexValidator

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

class TGS_Weeks(models.Model):
    date=models.DateField()
    match_type=models.CharField(max_length=5)
    fees=models.DecimalField(decimal_places=2,max_digits=7)
    total_games=models.IntegerField()

    def __str__(self):
        return str(self.date)+' '+self.match_type

class Djoin(models.Model):
    date_time=models.DateTimeField()
    cid=models.IntegerField()
    team_name=models.CharField(max_length=50)
    leader_pname=models.CharField(max_length=50)
    second_pname=models.CharField(max_length=50)
    third_pname=models.CharField(max_length=50)
    fourth_pname=models.CharField(max_length=50)
    fifth_pname=models.CharField(max_length=50)
    phone_valid=RegexValidator(regex='^\d{10}$')
    whats_num=models.CharField(validators=[phone_valid],max_length=10)
    email=models.EmailField(blank=True, null=True)
    pay_ss=models.ImageField(upload_to="djoin/pss/")
    team_logo=models.ImageField(upload_to="djoin/logo/",blank=True, null=True)

    def __str__(self):
        return str(self.cid)+' '+self.team_name

class Wjoin(models.Model):
    date_time=models.DateTimeField()
    cid=models.IntegerField()
    team_name=models.CharField(max_length=50)
    leader_pname=models.CharField(max_length=50)
    second_pname=models.CharField(max_length=50)
    third_pname=models.CharField(max_length=50)
    fourth_pname=models.CharField(max_length=50)
    fifth_pname=models.CharField(max_length=50)
    phone_valid=RegexValidator(regex='^\d{10}$')
    whats_num=models.CharField(validators=[phone_valid],max_length=10)
    email=models.EmailField(blank=True, null=True)
    pay_ss=models.ImageField(upload_to="wjoin/pss/")
    team_logo=models.ImageField(upload_to="wjoin/logo/",blank=True, null=True)

    def __str__(self):
        return str(self.cid)+' '+self.team_name

class Mjoin(models.Model):
    date_time=models.DateTimeField()
    cid=models.IntegerField()
    team_name=models.CharField(max_length=50)
    leader_pname=models.CharField(max_length=50)
    second_pname=models.CharField(max_length=50)
    third_pname=models.CharField(max_length=50)
    fourth_pname=models.CharField(max_length=50)
    fifth_pname=models.CharField(max_length=50)
    phone_valid=RegexValidator(regex='^\d{10}$')
    whats_num=models.CharField(validators=[phone_valid],max_length=10)
    email=models.EmailField(blank=True, null=True)
    pay_ss=models.ImageField(upload_to="mjoin/pss/")
    team_logo=models.ImageField(upload_to="mjoin/logo/",blank=True, null=True)

    def __str__(self):
        return str(self.cid)+' '+self.team_name