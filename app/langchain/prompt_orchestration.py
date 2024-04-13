from langchain.prompts import PromptTemplate

from app.common.text import PromptAgentConst
from app.common.consts import TextAgentConst

class SystemPromptGenerator:
    """
    This class is responsible for generating system prompts.
    """

    def __init__(self):
        """
        Initialize the SystemPromptGenerator with text, constants and a prompt template.
        """
        self.text = PromptAgentConst()
        self.consts = TextAgentConst()
        self.prompt_template = PromptTemplate()

    def prompt_tool_orchestration(self):
        """
        Generate a tool orchestration prompt.

        Returns:
            str: The generated prompt.
        """
        return self.text.tool_orchestration()

    def prompt_chain_mlops(self, data_context=None):
        """
        Generate a MLOps prompt.

        Args:
            data_context (dict, optional): The data context for the prompt. Defaults to 'mlops'.

        Returns:
            str: The generated prompt.
        """
        data_context = self.consts['mlops'] if data_context is None else data_context
        return self.prompt_template.format(data_context=data_context)

    def prompt_chain_data_engineering(self, data_context=None):
        """
        Generate a data engineering prompt.

        Args:
            data_context (dict, optional): The data context for the prompt. Defaults to 'data_engineering'.

        Returns:
            str: The generated prompt.
        """
        data_context = self.consts['data_engineering'] if data_context is None else data_context
        return self.prompt_template.format(data_context=data_context)

    def prompt_chain_ml_engineering(self, data_context=None):
        """
        Generate a machine learning engineering prompt.

        Args:
            data_context (dict, optional): The data context for the prompt. Defaults to 'machine_learning_engineering'.

        Returns:
            str: The generated prompt.
        """
        data_context = self.consts['machine_learning_engineering'] if data_context is None else data_context
        return self.prompt_template.format(data_context=data_context)

    def prompt_chain_data_science(self, data_context=None):
        """
        Generate a data science prompt.

        Args:
            data_context (dict, optional): The data context for the prompt. Defaults to 'data_science'.

        Returns:
            str: The generated prompt.
        """
        data_context = self.consts['data_science'] if data_context is None else data_context
        return self.prompt_template.format(data_context=data_context)


