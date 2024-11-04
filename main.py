# Implement Agentic AI for Customer Service
# Setup functions and indexes

# Setup Azure OpenAI connection
from llama_index.llms.azure_openai import AzureOpenAI
from llama_index.embeddings.azure_openai import AzureOpenAIEmbedding

from llama_index.core import Settings
import os
import nest_asyncio

nest_asyncio.apply()

api_key="<YOUR_API_KEY>"
azure_enpoint="https://<YOUR_ACCOUNT>.openai.azure.com/"
api_version="2024-05-01-preview"

# Function calling support only available in GPT-4
Settings.llm=AzureOpenAI(
	model="gpt-4",
	deployment_name="agentai-gpt4",
	api_key=api_key,
	azure_enpoint=azure_enpoint,
	api_version=api_version,
)

# Function calling support only available in GPT-4
Settings.llm=AzureOpenAI(
	model="gpt-4",
	deployment_name="agentai-gpt4",
	api_key=api_key,
	azure_enpoint=azure_enpoint,
	api_version=api_version,
)

Settings.embbed_model=AzureOpenAIEmbedding(
	model="text-embedding-ada-002",
	deployment_name="agentai-embedding",
    api_key=api_key,
    azure_endpoint=azure_endpoint,
    api_version=api_version,
)

from typing import List
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
from llama_index.core.node_parser import SentenceSplitter
from llama.core.tools import QueryEngineTool

#-----------------------------------------------------------
# Tool 1: Function that returns the list of items in order 
#-----------------------------------------------------------

def get_order_items(order_id: int) -> List[str]: 
    """ Given an order Id, this function returns the list of items purchased for that order"""
    order_items = {
        1001: ["Laptop","Mouse"],
        1002: ["Keyboard","HDMI Cable"],
        1003: ["Laptop","Keyboard"]
    }
    if order_id in order_items.keys():
        return order_items[order_id]
    else:
        return []
		
#--------------------------------------------------------------
# Tool 2: Functions that return the delivery date for an order
#--------------------------------------------------------------
def get_delivery_date(order_id : int) -> str:
    """ Given an order id, this function returns the delivery date for that order"""
    delivery_dates={
        1001: "10-Jun",
        1002: "12-Jun",
        1003: "08-Jun" 
    }
    
    if order_id in delivery_dates.keys():
        return delivery_dates[order_id]
    else:
        return ""

#---------------------------------------------------------------
# Tool 3: Function that returns maximum return days for an items
#---------------------------------------------------------------
def get_item_return_days(item: str) -> int:
    """ Given an Item, this function returns the return support for that
    order. The return support is in number of days
    """
    item_returns = {
        "Laptop": 30, 
        "Mouse": 15,
        "Keyboard": 15,
        "HDMI Cable": 5 
    }
    
    if item in item_returns.keys():
        return item_returns[item]
    else: 
        return 45 # Default days
        
#------------------------------------------------------------------
# Tool 4: Vector DB that contains customer support contacts
#------------------------------------------------------------------
# Setup vector index for return policies
support_docs = SimpleDirectoryReader(input_files=["Customer Service.pdf"]).load()

splitter = SentenceSplitter(chunk_size=1024)
support_nodes=splitter.get_nodes_from_documents(support_docs)
support_index=VectorStoreIndex(support_docs)
support_query_engine=support_index.as_query_engine()

# Setup the Customer Service AI Agent

from llama_index.core.tools import FunctionTool 

# Create tools for 3 functions and 1 index
order_item_tool = FunctionTool.from_defaults(fn=get_order_items)
delivery_date_tool=FunctionTool.from_defaults(fn=get_delivery_date)
return_policy_tool=FunctionTool.from_defaults(fn=get_item_return_days)

support_tool=QueryEngineTool.from_defaults(
    query_engine=support_query_engine,
    description=(
        "Customer support policies and contact information"
    ),
)
    
from llama_index.core.agent import FunctionCallingAgentWorker
from llama_index.core.agent import AgentRunner
from llama_index.llms.openai import OpenAI

# Setup the Agent worker in LlamaIndex with all the tools
# THis is the tool executor process
agent_worker = FunctionCallingAgentWorker.from_tools(
    [order_item_tool,
    delivery_date_tool,
    return_policy_tool,
    support_tool],
    llm=Settings.llm,
    verbose=True
)
# Calling an Agent Orchestrator with LlamaIndex
agent = AgentRunner(agent_worker)


# USing Customer Service Agent 
# get return policy for an order
response = agent.query(
"What is the return policy for order number 1001"
)
print("\n Final output: \n", response)


#
# Final output : 
# The return policy for order number 1001 is as follows:
# - Laptop: 30 days return policy
# - Mouse: 15 days return policy
#

# Three part question
response = agent.query("When is the delivery date and items shipped for order 1003 and how can I contact customer support?")

print("\n Final Output: \n", response)

#
# Final output : 
#  For order 1003, the items shipped are a Laptop and a Keyboard. The delivery date is scheduled for June 8th.

# If you need to contact customer support, you can call them at 1-987-654-3210 or email them at support@company.com.
  
# Question about an invalid order number
response = agent.query("What is return policy for order 1004")
print("\n Final Output: \n", response)

# Final output : 
# It seems that there are no items associated with order number 1004. Therefore, there is no return policy applicable for this order. If you believe this is an error or have any other inquiries, please let me know how I can assist you further!


  
