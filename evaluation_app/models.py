from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save

class Company(models.Model):
    """
    This Python code defines a model with fields for company name, type (selected from
    predefined choices), and approval status.
    :return: The `__str__` method in the provided code snippet is not returning anything
    explicitly. It should be updated to return a string representation of the object,
    typically by including the `name` attribute of the model. Here is an example of how it
    could be implemented:
    """
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
    """
    The code defines a model with fields for name, company (foreign key to Company model),
    and approval status in a Django application.
    :return: The `__str__` method in the provided code snippet is returning the `name`
    attribute of the model instance.
    """
    name = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    approval = models.BooleanField(default=False)

    def __str__(self):
        return self.name


@receiver(post_save, sender=Company)
@receiver(post_save, sender=Client)
def trigger_approval(sender, instance, created, **kwargs):
    """
    The function `trigger_approval` sets the approval status to True for a new instance and prints a
    message for demonstration purposes.
    
    :param sender: In the provided function `trigger_approval`, the parameters are as follows:
    :param instance: The `instance` parameter in the `trigger_approval` function refers to the instance
    of the model that triggered the signal. In Django, signals are used to allow decoupled applications
    to get notified when certain actions occur elsewhere in the application
    :param created: The `created` parameter in the `trigger_approval` function is a boolean value that
    indicates whether a new instance of a model has been created or an existing instance has been
    updated. It is typically used in Django signals to differentiate between creation and update
    operations on a model instance. In your function, the
    """
    if created:
        # trigger approval for instance
        instance.approval = True
        instance.save()
