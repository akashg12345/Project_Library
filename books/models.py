from django.db import models

# Create your models here.
class Active(models.Manager):   ## defining  custom model manager
    """Custom model Manager"""
    def get_queryset(self):     ## method overrriding
        return super(Active,self).get_queryset().filter(is_active ="N")

class books(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    quant = models.IntegerField()
    is_active = models.CharField(max_length=1,default="Y")

    objects = models.Manager()
    active = Active()

    

    class Meta:
        db_table = "book"
    
    def __str__(self) :
        return self.name

