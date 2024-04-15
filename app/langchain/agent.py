from langchain.agents import AgentExecutor, create_openai_tools_agent

class DataCrafterAgent:
    def __init__(self, model, tools, prompt):
        self.model = model
        self.tools = tools
        self.prompt = prompt
        self.agent = self.create_agent()
        self.agent_executor = AgentExecutor(agent=self.agent, tools=tools, verbose=True)

    def create_agent(self):
        return create_openai_tools_agent(self.model, self.tools, self.prompt)

    def invoke(self, input_text):
        return self.agent_executor.invoke(input_text)  


