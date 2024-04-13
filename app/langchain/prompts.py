from langchain.prompts import PromptTemplate

class SystemPromptGenerator:

    def __init__(self):
        self.prompt_template = PromptTemplate.from_template(
            "... {adjective} ... {content}."
        )

    def generate_prompt_1(self, adjective="funny", content="chickens"):
        return self.prompt_template.format(adjective=adjective, content=content)

    def generate_prompt_2(self, adjective="funny", content="chickens"):
        return self.prompt_template.format(adjective=adjective, content=content)

    def generate_prompt_3(self, adjective="funny", content="chickens"):
        return self.prompt_template.format(adjective=adjective, content=content)

