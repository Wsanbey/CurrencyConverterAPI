from django.db import models

# Create your models here.
class Currency(models.Model):
    code = models.CharField(max_length=3, unique=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.code

class ExchangeRate(models.Model):
    from_currency = models.ForeignKey(Currency, related_name='exchange_rates_from', on_delete=models.CASCADE)
    to_currency = models.ForeignKey(Currency, related_name='exchange_rates_to', on_delete=models.CASCADE)
    rate = models.DecimalField(max_digits=10, decimal_places=4)

    def __str__(self):
        return f"{self.from_currency} to {self.to_currency}: {self.rate}"