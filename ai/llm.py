from langchain.chat_models import init_chat_model
from env_config import Config

# Imports
groq_api_key = Config.GROQ_API_KEY
groq_model_name = Config.GROQ_MODEL_NAME
groq_model_provider = Config.GROQ_MODEL_PROVIDER

google_api_key = Config.GOOGLE_API_KEY
google_model_name = Config.GOOGLE_MODEL_NAME
google_model_provider = Config.GOOGLE_MODEL_PROVIDER

mistral_api_key = Config.MISTRAL_API_KEY
mistral_model_name = Config.MISTRAL_MODEL_NAME
mistral_model_provider = Config.MISTRAL_MODEL_PROVIDER

# GROQ LLM
def groq_llm(response: str):
    model = init_chat_model(
        api_key=groq_api_key, 
        model=groq_model_name, 
        model_provider=groq_model_provider
    )
    return model.invoke(response).content

# GOOGLE LLM
def google_llm(response: str):
    model = init_chat_model(
        api_key = google_api_key,
        model=google_model_name,
        model_provider=google_model_provider
    )
    return model.invoke(response).content

# MISTRAL LLM
def mistral_llm(response: str):
    model = init_chat_model(
        api_key = mistral_api_key,
        model=mistral_model_name,
        model_provider=mistral_model_provider
    )
    return model.invoke(response).content
