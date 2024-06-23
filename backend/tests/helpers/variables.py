medicine_shop_data = [
    {
        "name": "Panadol",
        "price": 100,
        "link": "https://www.dawaai.pk/panadol-500mg-tablet-10-s",
        "manufacturer": "GSK",
        "pack_details": "10 tablets",
        "image": "https://www.dawaai.pk/media/catalog/product/cache/1/image/9df78eab33525d08d6e5fb8d27136e95/p/a/panadol-500mg-tablet-10-s.jpg",
    },
    {
        "name": "Disprin",
        "price": 50,
        "link": "https://www.dawaai.pk/disprin-tablet-10-s",
        "manufacturer": "Reckitt Benckiser",
        "pack_details": "10 tablets",
        "image": "https://www.dawaai.pk/media/catalog/product/cache/1/image/9df78eab33525d08d6e5fb8d27136e95/d/i/disprin-tablet-10-s.jpg",
    },
    {
        "name": "Brufen",
        "price": 200,
        "link": "https://www.dawaai.pk/brufen-400mg-tablet-10-s",
        "manufacturer": "Abbott",
        "pack_details": "10 tablets",
        "image": "https://www.dawaai.pk/media/catalog/product/cache/1/image/9df78eab33525d08d6e5fb8d27136e95/b/r/brufen-400mg-tablet-10-s.jpg",
    },
]

medical_test_data = [
    {
        "name": "Blood Test",
        "price": 500,
        "link": "https://www.dawaai.pk/blood-test",
        "lab_name": "Chughtai Lab",
        "image": "https://pbs.twimg.com/profile_images/1522880282810015745/-Uax8id5_400x400.jpg",
    },
    {
        "name": "X-Ray",
        "price": 1000,
        "link": "https://www.dawaai.pk/x-ray",
        "lab_name": "Chughtai Lab",
        "image": "https://pbs.twimg.com/profile_images/1522880282810015745/-Uax8id5_400x400.jpg",
    },
    {
        "name": "MRI",
        "price": 2000,
        "link": "https://www.dawaai.pk/mri",
        "lab_name": "Chughtai Lab",
        "image": "https://pbs.twimg.com/profile_images/1522880282810015745/-Uax8id5_400x400.jpg",
    },
]


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

record_data = {
    "doctor_notes": "Test doctor note",
    "prescription": {
        "medicines": ["Medicine 1", "Medicine 2"],
        "tests": ["Test 1", "Test 2"],
    },
}


def get_record_prescription_data():
    from django.core.files.uploadedfile import SimpleUploadedFile

    with open("tests/test_files/prescription.png", "rb") as prescription:
        prescription_file = SimpleUploadedFile(
            prescription.name, prescription.read(), content_type="image/png"
        )

    return prescription_file
