from django.db import models


class Me(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth = models.IntegerField(default=2000)
    college = models.CharField(max_length=60)
    univerity = models.CharField(max_length=60)

    def __str__(self):
        return f" my name {self.first_name}"
