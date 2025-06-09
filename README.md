
# 🤖 Fun AI Chatbot – LangChain + Streamlit + OpenAI

A **conversational chatbot** that blends the power of OpenAI’s GPT with the structure of LangChain and the beauty of Streamlit – all topped with a dash of **humor**! 😄

![LangChain](https://img.shields.io/badge/LangChain-00A896?style=for-the-badge&logo=langchain&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

---

## 🎯 What’s This?

An interactive **Q&A chatbot** that:
- 🤹 Responds like a witty tech-savvy friend
- 💬 Remembers your questions and keeps the convo flowing
- 🌐 Runs on your local browser using Streamlit
- 🔐 Keeps your API keys safe with `.env`

---

## 🚀 Features

- 🔗 Powered by **LangChain** for structured prompt handling
- 🧠 Uses **OpenAI GPT-3.5** to generate responses
- 🧾 Maintains chat history with `st.session_state`
- 🎭 Acts like a **comedian AI assistant** for fun, engaging replies
- 🌈 Built using **Streamlit** for a clean UI experience

---

## 🏗️ Architecture

```

User Input → Streamlit UI → LangChain Messages → OpenAI → Funny AI Response → Display

````

---

## 🛠 Setup

### 1. Clone this repo
```bash
git clone https://github.com/SachinLoddiyaKarthik/Conversational-AI-Chatbot-with-LangChain-and-OpenAI
cd fun-ai-chatbot
````

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add your `.env` file

Create a file named `.env` in the root directory and add:

```env
OPENAI_API_KEY=your_openai_key_here
```

### 5. Run the app

```bash
streamlit run app.py
```

---

## 📸 Screenshot

> *Imagine a clean interface with a snarky bot giving witty answers to “What is LangChain?”* 😄

---

## 📦 Tech Stack

| Tool          | Role                      |
| ------------- | ------------------------- |
| Python        | Backend Logic             |
| Streamlit     | Web UI Framework          |
| LangChain     | LLM Prompt Management     |
| OpenAI        | Language Model Provider   |
| python-dotenv | Secure API Key Management |

---

## ✨ Sample Chat

```
You: What is LangChain?
Bot: Think of LangChain as the duct tape for AI apps – it holds your prompts, models, and logic together without falling apart mid-sentence.
```

---

## 🤝 Contributions

Got ideas? Bugs? Jokes?
Submit a PR or open an issue – let's make this chatbot smarter and funnier!

---

## 📬 Author

**Sachin Loddiya Karthik**
🔗 [GitHub](https://github.com/SachinLoddiyaKarthik) • [LinkedIn](https://www.linkedin.com/in/sachin-lk/)

---

## ⭐ Show Some Love

If this made you smile **or** learn something new, drop a ⭐ on the repo!

---
