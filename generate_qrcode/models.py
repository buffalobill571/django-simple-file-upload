from django.db import models


def upload_location(instance, filename):
    return "%s/%s" % (instance, filename)

class Some(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to=upload_location, null=True, blank=True)
