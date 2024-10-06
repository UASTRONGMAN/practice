from datetime import datetime

from django.core import validators as V
from django.db import models

from core_app.models import BaseModel

from apps.auto_parks.models import AutoParkModel
from apps.cars.choices import BodyTypeChoice
from apps.cars.managers import CarManager
from apps.cars.regex import CarRegex


class CarModel(BaseModel):
    class Meta:
        db_table = 'cars'
    model = models.CharField(max_length=50, validators=[V.RegexValidator(*CarRegex.MODEL.value)])
    body_type = models.CharField(max_length=50, choices=BodyTypeChoice.choices)
    price = models.IntegerField(validators=[V.MinValueValidator(1), V.MaxValueValidator(1000000)])
    year = models.IntegerField(validators=[V.MinValueValidator(1900), V.MaxValueValidator(datetime.now().year)])
    auto_park = models.ForeignKey(AutoParkModel, on_delete=models.CASCADE, related_name='cars')
    photo = models.ImageField(upload_to='storage', blank=True)

    objects = CarManager()
