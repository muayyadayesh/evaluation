from django.db import models

class Company(models.Model):
    COMPANY_TYPES = (
        ('SB', 'Small Business'),
        ('SU', 'Startup'),
        ('CO', 'Corporate'),
    )
    
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=2, choices=COMPANY_TYPES)
    approval = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Client(models.Model):
    name = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    approval = models.BooleanField(default=False)

    def __str__(self):
        return self.name
