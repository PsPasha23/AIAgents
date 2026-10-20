import streamlit as st
from llm_service import ask_ai

st.set_page_config(page_title="AI Tutor", page_icon="🤖", layout="centered")
st.title("🤖 AI Tutor Chat Assistant")
st.write("Welcome to the AI Tutor! Type your questions below and get explanations in simple terms.")

SYSTEM_PROMPT = """
You are a friendly AI tutor for beginners. Explain concepts in simple terms and provide simple examples. 
Avoid using technical jargon unless necessary, and always provide clear explanations.
"""

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "system", 
            "content": SYSTEM_PROMPT
        }
    ]
    
for message in st.session_state.messages:
    if message["role"] == "system":
        continue  # Skip displaying system messages
    
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        
model_choice = st.selectbox(
    "Which OpenAI model would you like to use?",
    options=["gpt-4.1-mini", "gpt-6-luna"],
    index=None,                      # nothing selected by default
    placeholder="Choose a model...",
)

user_input = st.chat_input(
    "Type your question here..." if model_choice else "Select a model above first",
    disabled=model_choice is None,   # the "wait" happens here
)
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    with st.chat_message("user"):
        st.markdown(user_input)
    
    with st.spinner("AI Tutor is thinking..."):
        with st.markdown("AI Tutor is thinking..."):
            response = ask_ai(st.session_state.messages, model_choice)
            st.markdown(response)
    
    st.session_state.messages.append({"role": "assistant", "content": response})