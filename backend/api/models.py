from django.db import models

class Currency(models.Model):
    code = models.CharField(max_length=3, unique=True)
    rate = models.DecimalField(max_digits=20, decimal_places=6)
    date = models.DateField()

    def __str__(self):
        return f"{self.code}: {self.rate}"
