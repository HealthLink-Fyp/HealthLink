from patient.models import MedicineShop, MedicalTest


def check_initial_data():
    """
    Check if the initial data is already present in the database.
    """
    return MedicineShop.objects.exists() and MedicalTest.objects.exists()


def populate_medical_data():
    """
    Populate the medical data in the database.
    """
    import json

    with open("healthlink/dbm/data/medical_tests.json") as file:
        medical_tests = json.load(file)

    for medical_test in medical_tests:
        MedicalTest.objects.create(**medical_test)

    if MedicalTest.objects.count() == len(medical_tests):
        return f"{len(medical_tests)} medical tests added to the database."

    with open("healthlink/dbm/data/medicines.json") as file:
        medicines = json.load(file)

    for medicine in medicines:
        MedicineShop.objects.create(**medicine)

    if MedicineShop.objects.count() == len(medicines):
        return f"{len(medicines)} medicines added to the database."

    return "Failed to add medical data to the database."
