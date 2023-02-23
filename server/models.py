from django.db import models

class waterpredictions(models.Model):
    date=models.DateField()
    time=models.TimeField()
    temperature = models.DecimalField(max_digits=15, decimal_places=7)
    humidity = models.IntegerField()
    soilMoisture=models.IntegerField()
    waterLevel=models.IntegerField()
    class Meta:
        verbose_name_plural = "WaterPredictions"
