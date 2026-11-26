from dotenv import load_dotenv
load_dotenv()

from langchain_core.tools import tool
from langchain_groq import ChatGroq
from langchain_tavily import TavilySearch



@tool
def triple(num:float)->float:
    """
    param num: a number to triple
    return: the triple of the input number
    """

    return float(num)*3


tools = [TavilySearch(max_results=1) , triple]

llm = ChatGroq(modle="openai/gpt-oss-20b" , temperature=0).bind_tools(tools)