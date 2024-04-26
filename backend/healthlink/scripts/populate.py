from patient.models import MedicineShop


def check_initial_medicines():
    """
    Check if the database is empty.
    """
    return MedicineShop.objects.exists()


def populate_medicines():
    """
    Populate the medicines in the database.
    """
    import json

    with open("healthlink/scripts/data/medicines.json") as file:
        medicines = json.load(file)

    for medicine in medicines:
        MedicineShop.objects.create(**medicine)

    if MedicineShop.objects.count() == len(medicines):
        return f"{len(medicines)} medicines added to the database."
    return "Failed to add medicines to the database."
