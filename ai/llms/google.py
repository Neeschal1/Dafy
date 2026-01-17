from langchain.chat_models import init_chat_model
from env_config import Config
from rest_framework.response import Response

google_api_key = Config.GOOGLE_API_KEY
google_model_name = Config.GOOGLE_MODEL_NAME
google_model_provider = Config.GOOGLE_MODEL_PROVIDER

def google_llm(response: str):
    model = init_chat_model(
        api_key = google_api_key,
        model=google_model_name,
        model_provider=google_model_provider
    )
    return Response({"Message":model.invoke(response).content})
