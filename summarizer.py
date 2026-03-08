from langchain_community.chat_models import ChatOllama
from langchain_core.messages import HumanMessage

llm = ChatOllama(model="llama3")

def summarize_text(text):
    text = text[:1500]   # limit article size
    prompt = f"Summarize the following text:\n\n{text}"

    response = llm.invoke([HumanMessage(content=prompt)])

    return response.content