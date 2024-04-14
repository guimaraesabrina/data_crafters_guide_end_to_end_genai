from langchain.prompts import PromptTemplate
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

from app.common.text import PromptAgentConst
from app.common.consts import TextAgentConst

class SystemPromptGenerator:
    def __init__(self):
        self.text = PromptAgentConst()
        self.consts = TextAgentConst()
        self.templates = {
            'mlops': PromptTemplate.from_template(
                "You are a tool focused on the theme in MLOps. "
                "Your role is to act as a friendly expert on the subject, ready to assist and guide users with emojis and helpful insights."
            ),
            'data_engineering': PromptTemplate.from_template(
                "You are a tool focused on the theme in Data Engineering. "
                "Your role is to act as a friendly expert on the subject, ready to assist and guide users with emojis and helpful insights."
            ),
            'machine_learning_engineering': PromptTemplate.from_template(
                "You are a tool focused on the theme in Machine Learning Engineering. "
                "Your role is to act as a friendly expert on the subject, ready to assist and guide users with emojis and helpful insights."
            ),
            'data_science': PromptTemplate.from_template(
                "You are a tool focused on the theme in Data Science. "
                "Your role is to act as a friendly expert on the subject, ready to assist and guide users with emojis and helpful insights."
            )
        }

    def prompt_agent_description(self):
        """
        Create and retrieve a structured prompt template for the agent.

        Returns:
            ChatPromptTemplate: The structured prompt for agent interaction.
        """
        agent_description = self.text.prompt_agent()
        
        return ChatPromptTemplate.from_messages([
            ("system", agent_description), 
            ("user", "{input}"),  
            MessagesPlaceholder(variable_name="agent_scratchpad")  
        ])

    def get_prompt_function(self, category):
        """
        Get a callable function that returns a formatted prompt based on the category.

        Args:
            category (str): The category of the prompt (mlops, data_engineering, etc.)

        Returns:
            function: A function that when called, returns a formatted prompt string.
        """
        # Retrieve the prompt template for the given category
        template = self.templates.get(category)

        # If the template exists, return a lambda function that simply returns the formatted prompt
        if template:
            return lambda: template.format()  # No more need to pass 'data_theme'
        
        # If no template is found for the category, return a default message
        return lambda: "No template found for category: {}".format(category)

