from django.db import models
from django.core.validators import RegexValidator


# Create your models here.
class Citizen(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    pin = models.CharField(unique=True, max_length=11,
                           validators=[RegexValidator(regex='^[0-9]{11}$', message='PIN has to be 11-digit number',
                                                      code='nomatch')])
    address = models.TextField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_address(self):
        context = {
            'pin': self.pin,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'address': self.address
        }
        return context
