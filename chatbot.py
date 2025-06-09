## Conversational Q&A Chatbot
import streamlit as st
from langchain.schema import HumanMessage, AIMessage, SystemMessage
from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv
import os

## Streamlit UI
st.set_page_config(page_title="Conversational Q&A Chatbot", page_icon=":robot:")
st.title("Conversational Q&A Chatbot")
st.write("Ask me anything about the world of AI and technology!")

# 🔐 Load your environment variables
load_dotenv()
openai_key = os.getenv("OPENAI_API_KEY")

if not openai_key:
    st.error("❌ Please set your OPENAI_API_KEY in the .env file.")
    st.stop()

# Initialize chat model
chat = ChatOpenAI(
    temperature=0.7,
    model="gpt-3.5-turbo",
    openai_api_key=openai_key
)

# Initialize message history
if 'flowmessages' not in st.session_state:
    st.session_state['flowmessages'] = [
        SystemMessage(content="You are a comedian AI assistant. You answer questions in a fun and engaging way, using humor and wit to keep the conversation lively. Your responses should be informative but also entertaining, making the user feel like they are chatting with a friend who knows a lot about technology and AI.")
    ]

# Get user input
user_question = st.text_input("Your Question:")

## Function to get chatbot response
def get_chatmodel_response(question):
    st.session_state['flowmessages'].append(HumanMessage(content=question))
    answer = chat(st.session_state['flowmessages'])
    st.session_state['flowmessages'].append(AIMessage(content=answer.content))
    return answer.content

# If Ask button is clicked
if st.button("Ask"):
    if user_question.strip():
        with st.spinner("Thinking..."):
            answer = get_chatmodel_response(user_question)
            st.success(answer)
    else:
        st.warning("⚠️ Please enter a question before submitting.")

# Display conversation history
st.markdown("### Conversation History")
for msg in st.session_state['flowmessages'][1:]:  # skip the system prompt
    if isinstance(msg, HumanMessage):
        st.markdown(f"**You:** {msg.content}")
    elif isinstance(msg, AIMessage):
        st.markdown(f"**Bot:** {msg.content}")

st.markdown("---")
st.markdown("Made with ❤️ by **[Sachin]**")
# Add a footer
st.markdown(
    """
    <style>
        footer {
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            background-color: #f1f1f1;
            text-align: center;
            padding: 10px;
        }
    </style>
    <footer>
        <p>© 2023 Conversational Q&A Chatbot. All rights reserved.</p>
    </footer>
    """,
    unsafe_allow_html=True
)
# Add a sidebar with instructions
st.sidebar.header("Instructions")       