from langchain.prompts import PromptTemplate

from app.common.text import PromptAgentConst
from app.common.consts import TextAgentConst

text = PromptAgentConst()
consts = TextAgentConst()

class SystemPromptGenerator:

    def __init__(self):
        self.prompt_template = PromptTemplate.from_template(text.tool_orchestartion())

    def prompt_chain_mlops(self, data_context=consts['mlops']):
        return self.prompt_template.format(data_context=data_context)

    def prompt_chain_data_engineering(self, data_context=consts['data_engineering']):
        return self.prompt_template.format(data_context=data_context)

    def prompt_chain_ml_engineering(self, data_context=consts['machine_learning_engineering']):
        return self.prompt_template.format(data_context=data_context)

    def prompt_chain_data_science(self, data_context=consts['data_science']):
        return self.prompt_template.format(data_context=data_context)
    
    