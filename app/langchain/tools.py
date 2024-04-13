from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.tools import tool

from app.setup.model import GenerativeModel
from estudos.data_crafters_guide_end_to_end_genai.app.langchain.prompt_orchestration import SystemPromptGenerator

output_parser = StrOutputParser()

model = GenerativeModel()
system_prompts = SystemPromptGenerator()

class CrafterTools:
    """
    This class contains tools for crafting data engineering, ML engineering, MLOps, and data science chains.
    """

    def __init__(self):
        """
        Initialize CrafterTools with a generative model and a string output parser.
        """
        self.model = GenerativeModel()
        self.output_parser = StrOutputParser()

    @tool
    def chain_data_engineering(self, input_text: str) -> str:
        """
        Craft a data engineering chain.

        Args:
            input_text (str): The input text.

        Returns:
            str: The result of invoking the chain.
        """
        prompt = ChatPromptTemplate.from_messages([
            ("system", system_prompts.prompt_chain_data_engineering),
            ("user", "{input}")
        ])

        chain = prompt | self.model | self.output_parser

        return chain.invoke({"input": input_text})

    @tool
    def chain_ml_engineering(self, input_text: str) -> str:
        """
        Craft a ML engineering chain.

        Args:
            input_text (str): The input text.

        Returns:
            str: The result of invoking the chain.
        """
        prompt = ChatPromptTemplate.from_messages([
            ("system", system_prompts.prompt_chain_ml_engineering),
            ("user", "{input}")
        ])

        chain = prompt | self.model | self.output_parser

        return chain.invoke({"input": input_text})

    @tool
    def chain_mlops(self, input_text: str) -> str:
        """
        Craft a MLOps chain.

        Args:
            input_text (str): The input text.

        Returns:
            str: The result of invoking the chain.
        """
        prompt = ChatPromptTemplate.from_messages([
            ("system", system_prompts.prompt_chain_mlops),
            ("user", "{input}")
        ])

        chain = prompt | self.model | self.output_parser

        return chain.invoke({"input": input_text})

    @tool
    def chain_data_science(self, input_text: str) -> str:
        """
        Craft a data science chain.

        Args:
            input_text (str): The input text.

        Returns:
            str: The result of invoking the chain.
        """
        prompt = ChatPromptTemplate.from_messages([
            ("system", system_prompts.prompt_chain_data_science),
            ("user", "{input}")
        ])

        chain = prompt | self.model | self.output_parser

        return chain.invoke({"input": input_text})

tools = [CrafterTools()]