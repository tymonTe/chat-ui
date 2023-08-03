import os

DEFAULT_SYSTEM_PROMPT = os.getenv(
    "NEXT_PUBLIC_DEFAULT_SYSTEM_PROMPT",
    "You are ChatGPT, a large language model trained by OpenAI. Follow the user's instructions carefully. Respond using markdown.")

OPENAI_API_HOST = os.getenv("OPENAI_API_HOST", 'https://api.openai.com')

DEFAULT_TEMPERATURE = float(os.getenv("NEXT_PUBLIC_DEFAULT_TEMPERATURE", "1"))

OPENAI_API_TYPE = os.getenv("OPENAI_API_TYPE", 'openai')

OPENAI_API_VERSION = os.getenv("OPENAI_API_VERSION", '2023-03-15-preview')

OPENAI_ORGANIZATION = os.getenv("OPENAI_ORGANIZATION", '')

AZURE_DEPLOYMENT_ID = os.getenv("AZURE_DEPLOYMENT_ID", '')
