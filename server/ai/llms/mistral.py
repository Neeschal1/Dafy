from langchain.chat_models import init_chat_model
from env_config import Config
from rest_framework.response import Response

mistral_api_key = Config.MISTRAL_API_KEY
mistral_model_name = Config.MISTRAL_MODEL_NAME
mistral_model_provider = Config.MISTRAL_MODEL_PROVIDER

def mistral_llm(response: str):
    model = init_chat_model(
        api_key = mistral_api_key,
        model=mistral_model_name,
        model_provider=mistral_model_provider
    )
    return Response({"Message":model.invoke(response).content})
