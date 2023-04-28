from django.db import models

# Create your models here.

class Coolshot(models.Model):
    units=models.FloatField()
    food=models.CharField(max_length=350)
    patient=models.CharField(max_length=200)
    complete=models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.created_at
