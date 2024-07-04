from django.db import models

# Create your models here.


class ImageModel(models.Model):
    img = models.ImageField()

class Newborn(models.Model):
    dateOfBirth = models.DateField()
    timeOfBirth = models.TimeField()
    birthWeight = models.PositiveIntegerField()
    gender = models.IntegerField()
    fSkinTone = models.IntegerField()
    mSkinTone = models.IntegerField()
    kramer = models.IntegerField()
    jaundice = models.BooleanField()
    bilirubin = models.FloatField()
    foreheads = models.ManyToManyField(ImageModel)
    device = models.CharField(max_length=256)






