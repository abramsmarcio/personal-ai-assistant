import streamlit as st
from main import get_response

st.set_page_config(page_title="Groq Chatbot", layout="centered")
st.title("💬 Personal Chatbot",)
st.markdown("Ask Anything")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    role = "🧑‍💻 You" if msg["role"] == "user" else "🤖 Assistant"
    with st.chat_message(role):
        st.markdown(msg["content"])

user_input = st.chat_input("Type your message...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("🧑‍💻 You"):
        st.markdown(user_input)

    with st.chat_message("🤖 Assistant"):
        full_response = ""
        response_box = st.empty()
        for chunk in get_response(st.session_state.messages):
            full_response += chunk
            response_box.markdown(full_response + "▌")

        response_box.markdown(full_response)
        st.session_state.messages.append({"role": "assistant", "content": full_response})
