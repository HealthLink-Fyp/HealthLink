from django.db.models.signals import post_migrate, post_save
from django.dispatch import receiver
from scripts import populate

from django.contrib.auth.models import User


@receiver(post_migrate)
def populate_medicines(sender, **kwargs):
    """
    Populate the medicines in the database after migration.
    """
    if not populate.check_initial_medicines():
        populate_status = populate.populate_medicines()
        print(populate_status)


@receiver(post_save, sender=User)
def update_profile_city(sender, instance, **kwargs):
    """
    Update the city in the profile when the user is updated.
    """
    if instance.is_patient and hasattr(instance, "patient"):
        instance.patient.city = instance.city
        instance.patient.save()
    elif instance.is_doctor and hasattr(instance, "doctor"):
        instance.doctor.city = instance.city
        instance.doctor.save()
