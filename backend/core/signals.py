from django.db.models.signals import post_migrate, post_save
from django.dispatch import receiver
from healthlink.scripts.populate import check_initial_data, populate_medical_data

from django.contrib.auth.models import User


@receiver(post_migrate)
def populate_data(sender, **kwargs):
    """
    Populate the medical data in the database after the migration.
    """

    populate_medical_data() if not check_initial_data() else None


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
