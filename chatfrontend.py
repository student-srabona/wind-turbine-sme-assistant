
import streamlit as st
import chatbackend as glib
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

# Page settings
st.set_page_config(page_title="Nova Chatbot")
st.title("🤖 Nova Chatbot")

# Create the LLM once
if "llm" not in st.session_state:
    st.session_state.llm = glib.nova_llm()

# Create chat history once
if "history" not in st.session_state:
    st.session_state.history = [
        SystemMessage(
            content="You are a helpful assistant. Always use the previous conversation history to answer the user's questions."
        )
    ]

# Display previous messages
for message in st.session_state.history:
    if isinstance(message, HumanMessage):
        with st.chat_message("user"):
            st.markdown(message.content)

    elif isinstance(message, AIMessage):
        with st.chat_message("assistant"):
            st.markdown(message.content)

# Chat input
prompt = st.chat_input("Type your message here...")

if prompt:

    # Show user message
    with st.chat_message("user"):
        st.markdown(prompt)

    # Save user message
    st.session_state.history.append(HumanMessage(content=prompt))

    # Get response
    response = st.session_state.llm.invoke(st.session_state.history)

    # Show assistant response
    with st.chat_message("assistant"):
        st.markdown(response.content)

    # Save assistant response
    st.session_state.history.append(
        AIMessage(content=response.content)
    )