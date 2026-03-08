from langchain_community.chat_models import ChatOllama
from langchain_core.messages import HumanMessage

llm = ChatOllama(model="llama3")

def generate_report(query, summaries):

    combined = "\n".join(summaries)

    prompt = f"""
    Create a research report about: {query}

    Use these summaries:
    {combined}
    """

    response = llm.invoke([HumanMessage(content=prompt)])

    return response.content