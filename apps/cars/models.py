from django.db import models

from apps.auto_parks.models import AutoParkModel
from core_app.models import BaseModel


class CarModel(BaseModel):
    class Meta:
        db_table = 'cars'
    model = models.CharField(max_length=50)
    price = models.IntegerField()
    year = models.IntegerField()
    auto_park = models.ForeignKey(AutoParkModel, on_delete=models.CASCADE, related_name='cars')
