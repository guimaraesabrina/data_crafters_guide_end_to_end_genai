import os
from langchain_openai import AzureChatOpenAI

class GenerativeModel:

    def __init__(self):
        azure_endpoint = os.getenv('AZURE_ENDPOINT', "thtps://openai-unilever-ufs.openai.azure.com/")
        openai_api_version = os.getenv('OPENAI_API_VERSION', "2023-07-01-preview")
        openai_api_key = os.getenv('OPENAI_API_KEY', "b9f3f868137141f18bd90cd0ce5f31de")
        openai_api_type = os.getenv('OPENAI_API_TYPE', "azure")
        deployment_name = os.getenv('DEPLOYMENT_NAME', "gpt-4")
        temperature = os.getenv('TEMPERATURE', 0.0)

        self.model = AzureChatOpenAI(
            azure_endpoint = azure_endpoint,
            openai_api_version = openai_api_version,
            openai_api_key = openai_api_key,
            openai_api_type = openai_api_type,
            deployment_name = deployment_name,
            temperature = temperature)

    def get_model(self):
        return self.model



