from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.tools import tool

from app.setup.model import GenerativeModel

model = GenerativeModel()
output_parser = StrOutputParser()

class CrafterTools:

    def __init__(self):
        self.model = GenerativeModel()
        self.output_parser = StrOutputParser()

    @tool
    def chain_data_engineering(self, input_text) -> str:
        prompt = ChatPromptTemplate.from_messages([
            ("system", "You are world class technical documentation writer."),
            ("user", "{input}")
        ])

        chain = prompt | self.model | self.output_parser

        return chain.invoke({"input": input_text})

    @tool
    def chain_ml_engineering(self, input_text) -> str:
        prompt = ChatPromptTemplate.from_messages([
            ("system", "You are world class technical documentation writer."),
            ("user", "{input}")
        ])

        chain = prompt | self.model | self.output_parser

        return chain.invoke({"input": input_text})

    @tool
    def chain_mlops(self, input_text) -> str:
        prompt = ChatPromptTemplate.from_messages([
            ("system", "You are world class technical documentation writer."),
            ("user", "{input}")
        ])

        chain = prompt | self.model | self.output_parser

        return chain.invoke({"input": input_text})

    @tool
    def chain_data_science(self, input_text) -> str:
        prompt = ChatPromptTemplate.from_messages([
            ("system", "You are world class technical documentation writer."),
            ("user", "{input}")
        ])

        chain = prompt | self.model | self.output_parser

        return chain.invoke({"input": input_text})

tools = CrafterTools()
