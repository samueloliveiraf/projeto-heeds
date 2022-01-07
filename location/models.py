from django.contrib.gis.db import models
from django.contrib.gis.geos import Point


class Location(models.Model):
    name = models.CharField(max_length=200)
    time = models.DateTimeField()
    latitude = models.FloatField()
    longitude = models.FloatField()

    point = models.PointField(
        blank=True,
        null=True,
        spatial_index=True
    )


    def save(self, *args, **kwargs):

        if self.longitude and self.latitude:

            self.point = Point(
                float(self.longitude),
                float(self.latitude),
                srid=4326
            )

        else:
            self.point = None
        super().save(*args, **kwargs)


    def __str__(self):
        return self.name

    
    def datetime(self):
        date = self.time
        date = date.strftime('%d/%m/%Y')

        return date

