from django.db import models

# Create your models here.


class Pet(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True, serialize=True)
    name = models.CharField(max_length=128, null=False)
    price = models.FloatField(null=False)
    pet_type = models.CharField(max_length=50, null=False)


