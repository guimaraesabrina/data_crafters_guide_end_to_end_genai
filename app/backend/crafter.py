from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from langchain_openai import AzureChatOpenAI

from app.langchain.tools import CrafterTools
from app.langchain.prompt_orchestration import SystemPromptGenerator
from app.langchain.agent import DataCrafterAgent


tools = CrafterTools()
prompt_system = SystemPromptGenerator()

tools = tools.tools 

model = AzureChatOpenAI(
            azure_endpoint = os.getenv('OPENAI_BASE'),
            openai_api_version = os.getenv('OPENAI_VERSION'),
            openai_api_key = os.getenv('OPENAI_KEY'),
            openai_api_type = os.getenv('OPENAI_TYPE'),
            deployment_name = os.getenv('OPENAI_DEPLOYMENT_NAME'),
            temperature = 0.0)

prompt_object = prompt_system.prompt_agent_description()
agent = DataCrafterAgent(model=model, tools=tools, prompt=prompt_object)

app = FastAPI()

class Input(BaseModel):
    input_text: str

class Output(BaseModel):
    model_response: str

@app.post("/generate/agent", response_model=Output)
def running_generative_agent(data: Input):
    try:
        response_dict = agent.invoke(data.input_text)
        
        response_output = response_dict.get('output', 'No answers found.')

        return Output(model_response=response_output)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))






    

