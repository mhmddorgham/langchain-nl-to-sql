import os
from dotenv import load_dotenv
load_dotenv()
import streamlit as st
from openai import OpenAI
from langchain_utils import invoke_chain

st.title("Natural Language to SQL 🚀")

client = OpenAI(api_key=os.getenv('OPENAI_SECRET_KEY'))

# Set a default model
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.spinner("Generating response..."):
        with st.chat_message("assistant"):
            try:
                # Attempt to invoke the chain
                print("st.session_state.messages:: ", st.session_state.messages)
                response = invoke_chain(prompt, st.session_state.messages)
                st.markdown(response)
                st.session_state.messages.append({"role": "assistant", "content": response})
            except Exception as e:
                # Handle any exception that occurs
                st.markdown("**Error:** Please provide more details.")
                # Optionally, log the error for debugging
                print(f"Error occurred: {e}")
