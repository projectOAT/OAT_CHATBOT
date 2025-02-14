# agent.py

from langchain_community.agent_toolkits import create_sql_agent
from database import db
from llm import llm
import ctransformers
print("ctransformers is installed successfully!")

# Create SQL Agent
def create_agent():
    return create_sql_agent(llm, db=db, verbose=True)

agent_executor = create_agent()
