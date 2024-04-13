from langchain.agents import AgentExecutor, create_openai_tools_agent

class OpenAIToolsAgent:
    def __init__(self, model, tools, prompt):
        
        self.agent = create_openai_tools_agent(model, tools, prompt)
        self.agent_executor = AgentExecutor(agent=self.agent, tools=tools, verbose=True)

    def invoke(self, input_text):
        self.agent_executor.invoke({"input": input_text})
