from django.db import models

class Car(models.Model):

    id = models.AutoField(primary_key = True,)
    model = models.CharField(max_length = 60,)
    brand = models.ForeignKey("app.brand",on_delete=models.CASCADE)
    factory_year = models.IntegerField(blank = True,null = True)
    model_year = models.IntegerField(blank=  True,null = True)
    value = models.FloatField(blank = True,null = True)
    image = models.ImageField(upload_to='upload/%y/%m/%d/',null=True,blank=True)
    plate = models.CharField(max_length=10,blank=True,null=True)
    def __str__(self):
        return self.model

class Brand(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    


    
