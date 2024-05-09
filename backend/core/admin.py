from django.contrib import admin

# Register your models here.
from .models import User, Availability, DoctorProfile, PatientProfile
from chat.models import Call
from patient.models import Appointment, MedicalRecord, MedicineShop, MedicalTest

admin.site.register(User)
admin.site.register(Availability)
admin.site.register(DoctorProfile)
admin.site.register(PatientProfile)
admin.site.register(Call)
admin.site.register(Appointment)
admin.site.register(MedicalRecord)
admin.site.register(MedicineShop)
admin.site.register(MedicalTest)
