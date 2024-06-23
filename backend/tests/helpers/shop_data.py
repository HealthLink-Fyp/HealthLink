from patient.models import MedicineShop, MedicalTest
from .variables import medicine_shop_data, medical_test_data


def add_medicines():
    for data in medicine_shop_data:
        MedicineShop.objects.create(**data)

    if MedicineShop.objects.count() == len(medicine_shop_data):
        return


def add_medical_tests():
    for data in medical_test_data:
        MedicalTest.objects.create(**data)

    if MedicalTest.objects.count() == len(medical_test_data):
        return
