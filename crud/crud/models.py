from django.db import models

class crudst(models.Model):
    stname=models.CharField(max_length=100)
    stemail = models.CharField(max_length=100)
    staddress = models.CharField(max_length=100)
    stmobile = models.IntegerField()
    stnGender = models.CharField(max_length=100)

    def __str__(self):
        return self.stname