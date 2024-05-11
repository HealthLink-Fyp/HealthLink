from langchain_core.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI
from .utils import get_fake_anonymizer
from .prompt import prompt_template, prompt_template_dashboard
import json


def prompt_chain(anonymizer=None, prompt=None):
    """
    Create a chain of functions to process the transcription
    """

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

    if prompt:
        if anonymizer is None:
            chain = {"anonymized_text": chatopenai} | prompt | chatopenai
        else:
            chain = {"anonymized_text": anonymizer.anonymize} | prompt | chatopenai
    else:
        raise ValueError("Prompt is required")

    return chain


def send_transcription_to_chatbot(transcription: str) -> dict:
    """
    Send the transcription to the chatbot and get the response
    """

    anonymizer = get_fake_anonymizer()
    prompt = PromptTemplate.from_template(prompt_template)
    chain = prompt_chain(anonymizer=anonymizer, prompt=prompt)

    response = chain.invoke(transcription)

    # Check for response presence and status code
    if response is None:
        return {"error": "OpenAi response is None"}

    response_json = validate_response(response.content)
    return response_json


def send_transcription_to_chatbot_v2(llm_response: str) -> dict:
    """
    Send the transcription to the chatbot and get the response
    """

    anonymizer = get_fake_anonymizer()
    prompt = PromptTemplate.from_template(prompt_template_dashboard)
    chain = prompt_chain(anonymizer=anonymizer, prompt=prompt)

    response = chain.invoke(llm_response)

    # Check for response presence and status code
    if response is None:
        return {"error": "OpenAi response is None"}

    response_json = validate_response_v2(response.content)
    return response_json


def validate_response_v2(response: str) -> dict:
    try:
        response = response.replace("```json", "").replace("```", "").strip()
        response_json = json.loads(response)
    except json.JSONDecodeError:
        return {"symptoms": [], "conditions": []}

    required_keys = {"symptoms", "conditions"}

    response_json_keys = set(response_json.keys())

    missing_keys = required_keys - response_json_keys
    extra_keys = response_json_keys - required_keys

    # Check for missing or extra keys
    if missing_keys:
        return {"error": f"Invalid response from OpenAi, missing keys {missing_keys}"}
    elif extra_keys:
        return {"error": f"Invalid response from OpenAi, extra keys {extra_keys}"}

    return response_json


def validate_response(response: str) -> dict:
    try:
        response = response.replace("```json", "").replace("```", "").strip()
        response_json = json.loads(response)
    except json.JSONDecodeError:
        return {
            "key_points": [],
            "likely_diagnoses": [],
            "followup_questions": [],
        }

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
