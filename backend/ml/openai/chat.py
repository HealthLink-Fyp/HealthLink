from langchain_core.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI
from .utils import get_fake_anonymizer
from .prompt import prompt_template
import json


def get_prompt() -> PromptTemplate:
    return PromptTemplate.from_template(prompt_template)


def send_transcription_to_chatbot(transcription: str) -> dict:
    anonymizer = get_fake_anonymizer()
    prompt = get_prompt()

    chatopenai = ChatOpenAI(
        temperature=0.5,
        model="gpt-3.5-turbo-0125",
        response_format={"type": "json_object"},
    )

    chain = {"anonymized_text": anonymizer.anonymize} | prompt | chatopenai

    response = chain.invoke(transcription)

    # Check for response presence and status code
    if response is None:
        return {"error": "OpenAi response is None"}

    response_json = validate_response(str(response.content))
    return response_json


def validate_response(response: str) -> dict:
    response_json = json.loads(response, strict=False)

    required_keys = {"key_points", "likely_diagnoses", "followup_questions"}

    response_json_keys = set(response_json.keys())

    missing_keys = required_keys - response_json_keys
    extra_keys = response_json_keys - required_keys

    # Check for missing or extra keys
    if missing_keys:
        return {"error": f"Invalid response from OpenAi, missing keys {missing_keys}"}
    elif extra_keys:
        return {"error": f"Invalid response from OpenAi, extra keys {extra_keys}"}

    return response_json
