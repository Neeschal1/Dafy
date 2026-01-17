from rest_framework import serializers

# Serializers for short term chat with llm
class ConversationSerializers(serializers.Serializer):
    Message = serializers.CharField()