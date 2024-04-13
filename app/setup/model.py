import os

from langchain_openai import AzureChatOpenAI

class GenerativeModel:

    def __init__(self):
        self.model = AzureChatOpenAI(
            azure_endpoint = os.getenv('OPENAI_BASE'),
            openai_api_version = os.getenv('OPENAI_VERSION'),
            openai_api_key = os.getenv('OPENAI_KEY'),
            openai_api_type = os.getenv('OPENAI_TYPE'),
            deployment_name = os.getenv('OPENAI_DEPLOYMENT_NAME'),
            temperature = 0.0)

