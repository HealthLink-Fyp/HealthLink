from django.contrib import admin

# Register your models here.
from .models import DoctorProfile, PatientProfile, User, UserForgot, UserToken

admin.site.register(User)
admin.site.register(UserToken)
admin.site.register(UserForgot)
admin.site.register(DoctorProfile)
admin.site.register(PatientProfile)