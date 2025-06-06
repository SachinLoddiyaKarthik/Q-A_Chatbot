import os
from dotenv import load_dotenv
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.exceptions import OutputParserException

# 🔐 Load your environment variables
load_dotenv()
openai_key = os.getenv("OPENAI_API_KEY")

if not openai_key:
    st.error("❌ Please set your OPENAI_API_KEY in the .env file.")
    st.stop()

# ✅ Define a function to get a response
def get_response(question):
    try:
        chat_llm = ChatOpenAI(temperature=0.7, model="gpt-3.5-turbo", openai_api_key=openai_key)
        return chat_llm.invoke(question)
    except OutputParserException as e:
        return f"⚠️ Parsing error: {e}"
    except Exception as e:
        return f"❌ Error: {e}"

# 🎨 Streamlit UI
st.set_page_config(page_title="Q&A Chatbot", page_icon="🤖")
st.title("🤖 Q&A Chatbot using LangChain + OpenAI")
st.write("Ask me anything below and I'll try to answer!")

user_question = st.text_input("📌 Your Question:")

if st.button("Get Answer"):
    if user_question.strip():
        with st.spinner("Thinking..."):
            answer = get_response(user_question)
            st.success(answer)
    else:
        st.warning("⚠️ Please enter a question before submitting.")

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
        <p>© 2023 Q&A Chatbot. All rights reserved.</p>
    </footer>
    """,
    unsafe_allow_html=True
)
# Add a sidebar with instructions
st.sidebar.header("Instructions")
st.sidebar.write(
    """
    1. Enter your question in the input box.
    2. Click the "Get Answer" button.
    3. Wait for the response from the chatbot.
    
    If you encounter any issues, please check your OpenAI API key in the `.env` file.
    """
)
# Add a sidebar with links to documentation and resources
st.sidebar.header("Resources")
st.sidebar.write(
    """
    - [LangChain Documentation](https://python.langchain.com/docs/)
    - [OpenAI API Documentation](https://platform.openai.com/docs/api-reference)
    - [Streamlit Documentation](https://docs.streamlit.io/)
    
    For any questions or feedback, feel free to reach out!
    """
)
# Add a sidebar with a link to the GitHub repository
st.sidebar.header("GitHub Repository")
st.sidebar.markdown(
    """
    - [GitHub Repository](https://github.com/SachinLoddiyaKarthik)
    """
)
