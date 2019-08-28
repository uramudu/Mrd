from django.db import models
class Patient (models.Model):
    idno=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=30)
    Hb=models.CharField(max_length=30)
    GlbLevel=models.CharField(max_length=30)
    HlBac=models.CharField(max_length=30)
    Heatbeet=models.CharField(max_length=30)
    Oxeygenlevel=models.CharField(max_length=30)
    Bmi=models.CharField(max_length=30)
    def __str__(self):
        return str(self.idno)
class Detalis(models.Model):
    Name = models.CharField(max_length=30)
    Age = models.CharField(max_length=30)
    Gen = models.CharField(max_length=30)
    Phone = models.CharField(max_length=30)
    id = models.IntegerField(primary_key=True)
    City = models.CharField(max_length=30)
    Blood = models.CharField(max_length=30)
    Addres = models.CharField(max_length=30)
class Description(models.Model):
    Des=models.CharField(max_length=180)

class Pat(models.Model):
    Description= models.ImageField(upload_to='images/',)
    prescription= models.ImageField(upload_to='images/',)
    OtherAtachment= models.ImageField(upload_to='images/',)





