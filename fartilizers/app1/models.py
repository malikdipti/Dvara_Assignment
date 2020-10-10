from django.db import models

# Create your models here.
class CatagoryModel(models.Model):
    catid=models.IntegerField(primary_key=True)
    Typeofcatagory=models.CharField(max_length=50)

class SubcatagoryModel(models.Model):
    subid=models.AutoField(primary_key=True )
    catid=models.ForeignKey(CatagoryModel,on_delete=models.CASCADE)
    subcatagory=models.CharField(max_length=50)

class AllDeatilsModel(models.Model):
    aidno=models.AutoField(primary_key=True)
    catagory=models.CharField(max_length=30)
    subcatagory=models.CharField(max_length=40)
    types=models.CharField(max_length=30)


