from langchain.prompts import PromptTemplate

from app.common.text import PromptAgentConst
from app.common.consts import TextAgentConst

class SystemPromptGenerator:

    def __init__(self):
        self.text = PromptAgentConst()
        self.consts = TextAgentConst()
        self.prompt_template = PromptTemplate() 

    def prompt_tool_orchestration(self):
        return self.text.tool_orchestration()

    def prompt_chain_mlops(self, data_context=None):
        data_context = self.consts['mlops'] if data_context is None else data_context
        return self.prompt_template.format(data_context=data_context)

    def prompt_chain_data_engineering(self, data_context=None):
        data_context = self.consts['data_engineering'] if data_context is None else data_context
        return self.prompt_template.format(data_context=data_context)

    def prompt_chain_ml_engineering(self, data_context=None):
        data_context = self.consts['machine_learning_engineering'] if data_context is None else data_context
        return self.prompt_template.format(data_context=data_context)

    def prompt_chain_data_science(self, data_context=None):
        data_context = self.consts['data_science'] if data_context is None else data_context
        return self.prompt_template.format(data_context=data_context)


