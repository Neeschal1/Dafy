from ai.llms.groq import groq_llm

def chatting(query):
    prompt = query.validated_data['Message']
    return groq_llm(prompt)