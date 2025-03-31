from django.db import models

class BloodSugarReading(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    glucose_level = models.FloatField()
    eye_movement_data = models.JSONField()

    def __str__(self):
        return f'Reading at {self.timestamp}: {self.glucose_level} mg/dL'

class InsulinInjection(models.Model):
    reading = models.ForeignKey(BloodSugarReading, on_delete=models.CASCADE)
    amount = models.FloatField()
    injection_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Injection of {self.amount} units at {self.injection_time}'