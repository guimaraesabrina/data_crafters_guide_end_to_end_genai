from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.tools import tool

from app.setup.model import GenerativeModel
from estudos.data_crafters_guide_end_to_end_genai.app.langchain.prompt_orchestration import SystemPromptGenerator

output_parser = StrOutputParser()

model = GenerativeModel()
system_prompts = SystemPromptGenerator()

class CrafterTools:

    def __init__(self):
        self.model = GenerativeModel()
        self.output_parser = StrOutputParser()

    @tool
    def chain_data_engineering(self, input_text) -> str:
        prompt = ChatPromptTemplate.from_messages([
            ("system", system_prompts.prompt_chain_data_engineering),
            ("user", "{input}")
        ])

        chain = prompt | self.model | self.output_parser

        return chain.invoke({"input": input_text})

    @tool
    def chain_ml_engineering(self, input_text) -> str:
        prompt = ChatPromptTemplate.from_messages([
            ("system", system_prompts.prompt_chain_ml_engineering),
            ("user", "{input}")
        ])

        chain = prompt | self.model | self.output_parser

        return chain.invoke({"input": input_text})

    @tool
    def chain_mlops(self, input_text) -> str:
        prompt = ChatPromptTemplate.from_messages([
            ("system", system_prompts.prompt_chain_mlops),
            ("user", "{input}")
        ])

        chain = prompt | self.model | self.output_parser

        return chain.invoke({"input": input_text})

    @tool
    def chain_data_science(self, input_text) -> str:
        prompt = ChatPromptTemplate.from_messages([
            ("system", system_prompts.prompt_chain_data_science),
            ("user", "{input}")
        ])

        chain = prompt | self.model | self.output_parser

        return chain.invoke({"input": input_text})

tools = [CrafterTools()]
