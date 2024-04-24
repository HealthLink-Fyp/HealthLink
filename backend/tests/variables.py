user_profile_data = {
    "first_name": "demo_name",
    "last_name": "demo_name",
    "password": "user@123",
    "username": "demo",
    "city": "Demo City",
}


doctor_profile_data = {
    "specialization": "general_practice",
    "qualification": "mbbs",
    "experience_years": 5,
    "consultation_fees": 500,
    "summary": "Dr. John Doe is a Cardiologist in Delhi with 5 years of experience.",
    "wait_time": 15,
    "recommendation_percent": 90,
    "patients_count": 100,
    "reviews_count": 50,
    "availability_data": {
        "days": ["monday", "tuesday"],
        "start": "09:00",
        "end": "17:00",
    },
}


doctor_availability_data = {
    "day": doctor_profile_data["availability_data"]["days"][0],
    "start_time": doctor_profile_data["availability_data"]["start"],
    "end_time": doctor_profile_data["availability_data"]["end"],
}

patient_profile_data = {
    "age": 20,
    "sex": 0,
    "blood_group": "A+",
    "weight": 60,
    "height": 170,
}


def get_record_data():
    from django.core.files.uploadedfile import SimpleUploadedFile

    with open("tests/test_files/prescription.png", "rb") as prescription:
        prescription_file = SimpleUploadedFile(
            prescription.name, prescription.read(), content_type="image/png"
        )

    with open("tests/test_files/test.png", "rb") as test:
        test_file = SimpleUploadedFile(test.name, test.read(), content_type="image/png")

    return {
        "doctor_note": "Test doctor note",
        "llm_note": "Test llm note",
        "prescription": prescription_file,
        "test_result": test_file,
    }
