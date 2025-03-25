from django.db import models
from datetime import datetime,timedelta,date
from django.utils.html import format_html
# Create your models here.

    
class Contact(models.Model):
    name = models.CharField(max_length=200,unique=True,verbose_name="Nom")
    firstname = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    message = models.CharField(max_length=1000)

    def _str_(self):
        return self.name
    
    class Meta:
        db_table = 'contact'
        verbose_name = 'contact'
        verbose_name_plural  = 'contacts'

class jus(models.Model):
    name = models.CharField(max_length=50,unique=True)
    image = models.ImageField(upload_to='static/images',null=True,blank=True)
    price = models.IntegerField()
    ingredient = models.TextField()
    diabetic = models.BooleanField()
    date = models.DateField(null=True)

    def __str__(self):
        return self.name
    

    class Meta:
        verbose_name = 'jus'
        verbose_name_plural = 'jus'




    
