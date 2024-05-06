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

    model_kwargs = {
        "response_format": {"type": "json_object"},
    }

    chatopenai = ChatOpenAI(
        temperature=0.5,
        base_url="https://api.deepseek.com/v1",
        model_name="deepseek-chat",
        model_kwargs=model_kwargs,
        api_key="sk-ce808733b8474062ba622b73f3b634cb",
    )

    chain = {"anonymized_text": anonymizer.anonymize} | prompt | chatopenai

    response = chain.invoke(transcription)

    # Check for response presence and status code
    if response is None:
        return {"error": "OpenAi response is None"}

    response_json = validate_response(response.content)
    return response_json


def validate_response(response: str) -> dict:
    try:
        response = response.replace("```json", "").replace("```", "").strip()
        response_json = json.loads(response)
    except json.JSONDecodeError:
        return {"error": "Invalid response from OpenAi, could not parse JSON"}

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
