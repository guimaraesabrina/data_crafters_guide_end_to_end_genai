from langchain.agents import AgentExecutor, create_openai_tools_agent

class DataCrafterAgent:
    """
    Represents a Data Crafter Agent that interacts with DataCrafter tools.
    """

    def __init__(self, model, tools, prompt):
        """
        Initializes a new instance of the DataCrafterAgent class.

        Args:
            model (str): The model to be used by the agent.
            tools (list): The list of tools to be used by the agent.
            prompt (str): The prompt to be used by the agent.
        """
        self.agent = create_openai_tools_agent(model, tools, prompt)
        self.agent_executor = AgentExecutor(agent=self.agent, tools=tools, verbose=True)

    def invoke(self, input_text):
        """
        Invokes the agent with the given input text.

        Args:
            input_text (str): The input text to be processed by the agent.
        """
        self.agent_executor.invoke({"input": input_text})

