from django.db import models

# Create your models here.

class Phone(models.Model):
    brand = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    year = models.IntegerField()
    model = models.CharField(max_length=255)
    price = models.FloatField()

    def __str__(self):
        return 'Brand - {}, Name - {} {}, price - {}'.\
            format(self.brand,
                   self.name,
                   self.model,
                   self.price)

