from langchain.prompts import PromptTemplate

class SystemPromptGenerator:

    def __init__(self):
        self.prompt_template = PromptTemplate.from_template(
            "... {data_context}."
        )

    def prompt_chain_mlops(self, data_context="funny"):
        return self.prompt_template.format(data_context=data_context)

    def prompt_chain_data_engineering(self, data_context="funny"):
        return self.prompt_template.format(data_context=data_context)

    def prompt_chain_ml_engineering(self, data_context="funny"):
        return self.prompt_template.format(data_context=data_context)

    def prompt_chain_data_science(self, data_context="funny"):
        return self.prompt_template.format(data_context=data_context)

