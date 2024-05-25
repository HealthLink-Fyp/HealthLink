from langchain_core.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI
from .utils import get_fake_anonymizer
from .prompt import prompt_template, prompt_template_dashboard
import os
import dotenv
import json

# Load the LLM model configuration
dotenv.load_dotenv()

# Load the LLM model configuration from environment variables
MODEL_NAME = os.getenv("MODEL_NAME", "deepseek-chat")
API_KEY = os.getenv("API_KEY", "sk-ce808733b8474062ba622b73f3b634cb")
BASE_URL = os.getenv("BASE_URL", "https://api.deepseek.com/v1")

# Initialize the anonymizer and prompt templates
ANONYMIZER = get_fake_anonymizer()
PROMPT = PromptTemplate.from_template(prompt_template)
PROMPT_DASHBOARD = PromptTemplate.from_template(prompt_template_dashboard)


def chat_model(
    model_name: str = MODEL_NAME,
    api_key: str = API_KEY,
    base_url: str = BASE_URL,
) -> ChatOpenAI:
    """
    Create a chain of functions to process the transcription
    """

    model_kwargs = {
        "response_format": {"type": "json_object"},
    }

    model = ChatOpenAI(
        temperature=0.5,
        base_url=base_url,
        model_name=model_name,
        model_kwargs=model_kwargs,
        api_key=api_key,
    )
    
    return model


def prompt_response(transcription: str, model: dict) -> dict:
    """
    Send the transcription to the chatbot and get the response
    """

    chain = {"anonymized_text": ANONYMIZER} | PROMPT | model

    response = chain.invoke(transcription)
    
    return response


def send_transcription_to_chatbot(transcription: str) -> dict:
    """
    Send the transcription to the chatbot and get the response
    """
    if not PROMPT:
        return {"error": "Prompt is None"}
    
    if not ANONYMIZER:
        return {"error": "Anonymizer is None"}

    model = chat_model()

    response = prompt_response(transcription=transcription, model=model)

    # Check for response presence and status code
    if response is None:
        return {"error": "OpenAi response is None"}

    response_json = validate_response(response.content)
    return response_json


def send_transcription_to_chatbot_v2(llm_response: str) -> dict:
    """
    Send the transcription to the chatbot and get the response
    """

    if not PROMPT_DASHBOARD:
        return {"error": "Prompt is None"}
    
    if not ANONYMIZER:
        return {"error": "Anonymizer is None"}
    
    model = chat_model()

    response = prompt_response(llm_response, model)

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
