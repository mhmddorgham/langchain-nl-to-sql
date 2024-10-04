import os
from dotenv import load_dotenv

load_dotenv()

db_user = os.getenv("db_user")
db_password = os.getenv("db_password")
db_host = os.getenv("db_host")
db_name = os.getenv("db_name")


# Langsmith configurations
LANGCHAIN_TRACING_V2=os.getenv('LANGCHAIN_TRACING_V2')
LANGCHAIN_ENDPOINT=os.getenv('LANGCHAIN_ENDPOINT')
LANGCHAIN_API_KEY=os.getenv('LANGCHAIN_API_KEY')
LANGCHAIN_PROJECT=os.getenv('LANGCHAIN_PROJECT')



from langchain_community.utilities.sql_database import SQLDatabase
from langchain.chains import create_sql_query_chain
from langchain_openai import ChatOpenAI
from langchain_community.tools.sql_database.tool import QuerySQLDataBaseTool
# from langchain.memory import ChatMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory

from operator import itemgetter

from langchain_core.output_parsers import StrOutputParser

from langchain_core.runnables import RunnableLambda
from langchain_openai import ChatOpenAI


# from table_details import table_chain as select_table
from prompts import final_prompt, answer_prompt

import streamlit as st
@st.cache_resource
def get_chain():
    print("Creating chain...")
    db = SQLDatabase.from_uri(f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}")    
    llm = ChatOpenAI(api_key= os.getenv("OPENAI_SECRET_KEY"), model="gpt-3.5-turbo", temperature=0)
    generate_query = create_sql_query_chain(llm, db,final_prompt) 
    execute_query = QuerySQLDataBaseTool(db=db)
    rephrase_answer = answer_prompt | llm | StrOutputParser()
    chain = (
        RunnableLambda(lambda inputs: {"question": inputs["question"], "query": generate_query.invoke(inputs), "result": execute_query.invoke({"query": generate_query.invoke(inputs)})})
    ) | rephrase_answer


    return chain

def create_history(messages):
    print("Creating history...")
    history = ChatMessageHistory()
    for message in messages:
        if message["role"] == "user":
            history.add_user_message(message["content"])
        else:
            history.add_ai_message(message["content"])
    return history

def invoke_chain(question,messages):
    chain = get_chain()
    history = create_history(messages)
    response = chain.invoke({"question": question,"messages":history.messages})
    history.add_user_message(question)
    history.add_ai_message(response)
    return response


