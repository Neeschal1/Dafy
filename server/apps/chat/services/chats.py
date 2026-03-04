from ai.llms.groq import groq_llm_stream

def chatting_stream(query):
    prompt = query.validated_data['Message']
    return groq_llm_stream(prompt)