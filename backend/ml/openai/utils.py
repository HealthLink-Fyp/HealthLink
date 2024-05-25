from faker import Faker
from presidio_anonymizer.entities import OperatorConfig
from langchain_experimental.data_anonymizer import PresidioAnonymizer


def fake_phone_number(_=None) -> str:
    fake = Faker(locale="en_US")
    return fake.phone_number()


def get_fake_anonymizer() -> PresidioAnonymizer:
    phone_number_operator = {
        "PHONE_NUMBER": OperatorConfig("custom", {"lambda": fake_phone_number})
    }
    anonymizer = PresidioAnonymizer()
    anonymizer.add_operators(phone_number_operator)
    return anonymizer.anonymize
