import streamlit as st
import ollama

# Page configuration
st.set_page_config(
    page_title="AI Chatbot",
    page_icon="🤖",
    layout="centered"
)

# CSS
st.markdown("""
<style>

    /* Main background */
    .stApp {
        background-color: #f5f7fb;
    }

    /* Title */
    h1 {
        text-align: center;
        color: #4a4a4a;
        font-size: 40px;
        font-weight: 700;
        margin-bottom: 25px;
    }

    /* Chat messages */
    [data-testid="stChatMessage"] {
        border-radius: 15px;
        padding: 12px;
        margin: 8px 0;
    }

    /* Message text */
    [data-testid="stChatMessageContent"] {
        font-size: 16px;
        line-height: 1.6;
    }

    /* Chat input */
    [data-testid="stChatInput"] {
        border-radius: 15px;
    }

    /* Input text */
    [data-testid="stChatInput"] textarea {
        font-size: 16px;
    }

</style>
""", unsafe_allow_html=True)


# Title
st.title("AI Chatbot")


# Store messages
if "messages" not in st.session_state:
    st.session_state.messages = []


# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])


# User input
user_input = st.chat_input("Type your message...")


if user_input:

    # Add user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    # Display user message
    with st.chat_message("user"):
        st.write(user_input)


    # Get response from Ollama
    response = ollama.chat(
        model="llama3.2",
        messages=st.session_state.messages
    )

    bot_response = response["message"]["content"]


    # Add assistant response
    st.session_state.messages.append({
        "role": "assistant",
        "content": bot_response
    })


    # Display assistant response
    with st.chat_message("assistant"):
        st.write(bot_response)