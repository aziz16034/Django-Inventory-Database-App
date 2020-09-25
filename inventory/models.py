from django.db import models

# Create your models here.

class Devices(models.Model):
    type = models.CharField(max_length=10, blank=False)
    price = models.IntegerField()

    
    choices = (
         ('SOLD', 'Item already purchased'),
         ('AVAILABLE', 'Item ready to be purchased'),
         ('RESTOCKING', 'Item restocking in few days')
     )

    status = models.CharField(max_length=10,choices=choices, default="Sold")
    description = models.CharField(max_length=10, default="try")


    class Meta:
        abstract =True

    def __str__(self):
        return 'Type: {0} Price :{1}'.format(self.type,self.price)



class Laptop(Devices):
    pass

class Mobile(Devices):
    pass


class phone(Devices):
    pass

  