# ai_engine.py
"""
This file contains all AI/LLM logic.
We keep it separate so main.py stays clean and easy to manage.
"""

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

# Create and configure the OpenAI model
llm = ChatOpenAI(
    model="gpt-4o-mini",   
    temperature=0.7,
    max_completion_tokens=100,
    
)

# Create a reusable prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an AI content generator. Be helpful and creative. you will write with in 100 tokens"),
    ("human", "{input_text}")
])


def generate_content(user_text: str) -> str:
    """
    Generate AI output using LangChain + OpenAI.
    
    Args:
        user_text (str): Input from the user.

    Returns:
        str: AI-generated content.
    """

    chain = prompt | llm
    response = chain.invoke({"input_text": user_text})

    return response.content
