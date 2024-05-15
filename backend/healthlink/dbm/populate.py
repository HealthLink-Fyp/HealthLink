from patient.serializers import MedicineShopSerializer, MedicalTestSerializer
from core.serializers import (
    UserSerializer,
    DoctorProfileSerializer,
    PatientProfileSerializer,
)
import os
import json

# Paths and serializers
PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), "medical_data.json")
SERIALIZERS = [
    MedicineShopSerializer,
    MedicalTestSerializer,
    UserSerializer,
    DoctorProfileSerializer,
    PatientProfileSerializer,
]


def check_initial_data() -> bool:
    """
    Check if the initial data is already present in the database.
    """
    return all(serializer.Meta.model.objects.exists() for serializer in SERIALIZERS)


def load_JSON(file: str) -> dict:
    """
    Load the JSON file.
    """
    try:
        with open(file, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON in {file}")
        return {}


def populate_medical_data() -> None:
    """
    Populate the medical data in the database.
    """

    # Check if the required files are present
    if not os.path.isfile(PATH):
        raise FileNotFoundError(f"File not found: {PATH}")

    # Create a dictionary of serializers
    serializer_dict = {
        serializer.Meta.model.__name__: serializer for serializer in SERIALIZERS
    }

    # Load the data
    data = load_JSON(PATH)
    for key, items in data.items():
        serializer_class = serializer_dict.get(key)
        if serializer_class and not serializer_class.Meta.model.objects.exists():
            print(f"Populating {key} using {serializer_class.__name__} to database.")
            if serializer_class == DoctorProfileSerializer:
                for item in items:
                    serializer = serializer_class(data=item)
                    serializer.is_valid(raise_exception=True)
                    serializer.save()
            else:
                serializer = serializer_class(data=items, many=True)
                serializer.is_valid(raise_exception=True)
                serializer.save()
        else:
            print(f"Warning: {key} already exists in the database.")
