
ADMIN = 'admin'
DOCTOR = 'doctor'
PATIENT = 'patient'

ROLE_CHOICES = [
(ADMIN, 'Admin'),
(DOCTOR, 'Doctor'),
(PATIENT, 'Patient'),
]

SPECIALIZATION_CHOICES = (
        ('cardiologist', 'Cardiologist'),
        ('dentist', 'Dentist'),
        ('dermatologist', 'Dermatologist'),
        ('endocrinologist', 'Endocrinologist'),
        ('gastroenterologist', 'Gastroenterologist'),
        ('gynecologist', 'Gynecologist'),
        ('hematologist', 'Hematologist'),
        ('internist', 'Internist'),
        ('nephrologist', 'Nephrologist'),
        ('neurologist', 'Neurologist'),
        ('neurosurgeon', 'Neurosurgeon'),
        ('obstetrician', 'Obstetrician'),
        ('oncologist', 'Oncologist'),
        ('ophthalmologist', 'Ophthalmologist'),
        ('orthopedic surgeon', 'Orthopedic Surgeon'),
        ('otolaryngologist', 'Otolaryngologist'),
        ('pathologist', 'Pathologist'),
        ('pediatrician', 'Pediatrician'),
        ('physiatrist', 'Physiatrist'),
        ('podiatrist', 'Podiatrist'),
        ('psychiatrist', 'Psychiatrist'),
        ('pulmonologist', 'Pulmonologist'),
        ('radiologist', 'Radiologist'),
        ('rheumatologist', 'Rheumatologist'),
        ('surgeon', 'Surgeon'),
        ('urologist', 'Urologist'),
        ('other', 'Other'),
    )


QUALIFICATION_CHOICES = (
        ('mbbs', 'MBBS'),
        ('bds', 'BDS'),
        ('md', 'MD'),
        ('ms', 'MS'),
        ('dm', 'DM'),
        ('mch', 'MCH'),
        ('phd', 'PHD'),
        ('other', 'Other'),
)