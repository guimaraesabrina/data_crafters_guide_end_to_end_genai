from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.tools import tool

from app.setup.model import GenerativeModel
from app.langchain.prompt_orchestration import SystemPromptGenerator

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
        self.system_prompts = SystemPromptGenerator()

        # store references to tool methods in a list
        self.tools = [
            self.chain_data_engineering,
            self.chain_ml_engineering,
            self.chain_mlops,
            self.chain_data_science
        ]

    @tool
    def chain_data_engineering(self, input_text: str):
        """
        Designed as an expert in data engineering, 
        this tool offers guidance on efficient data management. 
        It answers questions and assists in developing optimized data pipelines, 
        facilitating effective data collection, integration, and processing
        """
        prompt = self.system_prompts.get_prompt_function('data_engineering')()

        chain = ChatPromptTemplate.from_messages([
            ("system", prompt),
            ("user", input_text)
        ]) | self.model | self.output_parser

        return chain.invoke()

    @tool
    def chain_ml_engineering(self, input_text: str):
        """
        This tool specializes in machine learning engineering, 
        supporting you from model design to evaluation. 
        It answers questions about algorithm selection, hyperparameter tuning, 
        and more, ensuring the development of efficient and effective ML solutions.
        """
        prompt = self.system_prompts.get_prompt_function('machine_learning_engineering')()
        chain = ChatPromptTemplate.from_messages([
            ("system", prompt),
            ("user", input_text)
        ]) | self.model | self.output_parser
        return chain.invoke()

    @tool
    def chain_mlops(self, input_text: str):
        """
        This specialized MLOps tool serves as your expert assistant 
        for managing machine learning operations. 
        It provides support by answering questions and guiding best practices for implementing 
        and scaling ML models efficiently in production environments.
        """
        prompt = self.system_prompts.get_prompt_function('mlops')()
        chain = ChatPromptTemplate.from_messages([
            ("system", prompt),
            ("user", input_text)
        ]) | self.model | self.output_parser
        return chain.invoke()

    @tool
    def chain_data_science(self, input_text: str):
        """
        Acting as a data science expert, this tool helps you navigate through data analysis, 
        machine learning, and statistical modeling. 
        It responds to inquiries, providing insights to transform raw data into 
        strategic decisions through advanced analysis and visualization
        """
        prompt = self.system_prompts.get_prompt_function('data_science')()
        chain = ChatPromptTemplate.from_messages([
            ("system", prompt),
            ("user", input_text)
        ]) | self.model | self.output_parser
        return chain.invoke()

    def available_chains(self):
        """
        Return a list of available chain functions.

        Returns:
            list: A list of function references representing available chains.
        """
        return self.tools

