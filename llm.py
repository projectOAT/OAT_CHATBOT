# llm.py

from langchain_community.llms import CTransformers
import config

# Load Llama 3 Model
def load_llm():
    return CTransformers(model=config.LLAMA_MODEL_PATH, model_type="llama")

llm = load_llm()
