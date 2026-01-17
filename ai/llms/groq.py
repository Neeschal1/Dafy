from langchain.chat_models import init_chat_model
from env_config import Config

groq_api_key = Config.GROQ_API_KEY
groq_model_name = Config.GROQ_MODEL_NAME
groq_model_provider = Config.GROQ_MODEL_PROVIDER

def groq_llm(response: str):
    model = init_chat_model(
        api_key=groq_api_key, 
        model=groq_model_name, 
        model_provider=groq_model_provider
    )
    return model.invoke(response).content
