from django.contrib import admin

# Register your models here.
from .models import DoctorProfile, PatientProfile, User, Availability

admin.site.register(User)
admin.site.register(Availability)
admin.site.register(DoctorProfile)
admin.site.register(PatientProfile)
