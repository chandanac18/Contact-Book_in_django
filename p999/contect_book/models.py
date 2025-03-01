from django.db import models

class contect(models.Model):
    name = models.CharField(max_length=255)
    phone = models.DecimalField(max_digits=10, decimal_places=2)
    email = models.EmailField(max_length=30, blank=True)
    date = models.DateField()


    def __str__(self):
        return self.name
