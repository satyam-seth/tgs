from django.db import models

# Create your models here.

class Daily(models.Model):
    d_date=models.DateField()
    d_type=models.CharField(max_length=5)
    d_fees=models.DecimalField(decimal_places=2,max_digits=7)
    d_tgames=models.IntegerField()

    def __str__(self):
        return str(self.d_date)+' '+self.d_type

class Weekly(models.Model):
    w_date=models.DateField()
    w_type=models.CharField(max_length=5)
    w_fees=models.DecimalField(decimal_places=2,max_digits=7)
    w_tgames=models.IntegerField()

    def __str__(self):
        return str(self.w_date)+' '+self.w_type

class Monthly(models.Model):
    m_date=models.DateField()
    m_type=models.CharField(max_length=5)
    m_fees=models.DecimalField(decimal_places=2,max_digits=7)
    m_tgames=models.IntegerField()

    def __str__(self):
        return str(self.m_date)+' '+self.m_type