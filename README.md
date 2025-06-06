
# 🧠 LangChain Chatbot with Streamlit

[![LangChain](https://img.shields.io/badge/LangChain-00A896?style=for-the-badge&logo=data:image/svg+xml;base64,...)](https://www.langchain.com/)
[![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white)](https://openai.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![HuggingFace](https://img.shields.io/badge/HuggingFace-FCC624?style=for-the-badge&logo=huggingface&logoColor=black)](https://huggingface.co/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org/)

## 🎯 Project Overview

A simple chatbot app built using **LangChain**, **OpenAI**, and **Streamlit**, with support for HuggingFace models and `.env`-based API authentication.

### 💡 Highlights

- 🔗 **LangChain framework** for prompt engineering and LLM abstraction
- 🤖 **OpenAI API** to generate human-like responses
- 📺 **Streamlit UI** for interactive web-based Q&A
- 🧠 **HuggingFace Hub** for additional embeddings and LLMs
- 🔐 **dotenv integration** to manage API keys securely

## 🏗️ Architecture

```
User Input → Streamlit UI → LangChain PromptTemplate → LLM (OpenAI) → Response Output
```

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/SachinLoddiyaKarthik/Q-A_Chatbot.git
cd langchain-chatbot
```

### 2. Set Up Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure `.env` File

Create a `.env` file and add your API key:

```env
OPENAI_API_KEY=your_openai_key_here
```

### 5. Run the App

```bash
streamlit run app.py
```

## 🛠 Tech Stack

| Tool         | Usage                                 |
|--------------|----------------------------------------|
| Python       | Programming language                   |
| Streamlit    | Frontend interface                     |
| LangChain    | Prompt engineering and LLM interface   |
| OpenAI       | LLM provider                           |
| HuggingFace  | Alternative models/embeddings          |
| dotenv       | Environment variable management        |

## ✨ Sample Output

```
User: What is LangChain?
Bot: LangChain is a framework for developing applications powered by language models.
```

## 🤝 Contributing

Feel free to fork, enhance, and open PRs. Star ⭐ the repo if you find it helpful!

## 📞 Contact

- **GitHub**: [SachinLoddiyaKarthik](https://github.com/SachinLoddiyaKarthik)
- **LinkedIn**: [Connect with me](https://www.linkedin.com/in/sachin-lk/)
