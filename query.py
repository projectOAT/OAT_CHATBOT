# query.py

from agent import agent_executor

# Ask a sample question
question = "What is the highest mark in Mathematics?"
response = agent_executor.invoke(question)

print("Answer:", response)
