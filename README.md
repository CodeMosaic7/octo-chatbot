
# 🗣️ Personal Voice Chatbot for Manika

This project is a **voice-enabled personal assistant chatbot** built using **LangChain**, **Ollama (LLaMA 3.2:1b)**, and **Streamlit**. It can carry on intelligent, memory-aware conversations with a friendly, concise tone — just like a real assistant. Conversations are stored locally for continuity across sessions.

---

## 🚀 Features

- ✅ **Locally running LLM** via [Ollama](https://ollama.com/)
- 🧠 **Memory support** with file-based chat history
- 🎤 **Voice input/output** (via `speech_recognition` and `pyttsx3`)
- 💬 **Streamlit web interface** for easy interaction
- 🧱 Modular LangChain structure for easy extension

---

## 🛠️ Technologies Used

- [LangChain](https://www.langchain.com/)
- [Ollama](https://ollama.com/) with `llama3.2:1b`
- [Streamlit](https://streamlit.io/)
- `speech_recognition` for voice input
- `pyttsx3` for voice output
- `Python 3.10+`

---

## 📁 Project Structure

```

chatbot/
│
├── main.py                       # Streamlit app
├── speaking\_bot/
│   ├── setup.py                  # Initializes ConversationChain with memory
│   └── voice\_utils.py            # Voice input/output functions
├── chat\_history.txt              # Local conversation memory file
├── requirements.txt
└── README.md

````

---

## ▶️ How to Run

### 1. 🧠 Install Dependencies

```bash
pip install -r requirements.txt
````

Make sure `ollama` is installed and running:

```bash
ollama run llama3
```

### 2. 🏃‍♀️ Launch the App

```bash
streamlit run main.py
```

---

## 🔊 Voice Commands

You can speak to the assistant using your microphone. The assistant will:

* Transcribe your speech to text
* Respond with both **text** and **spoken voice**

---

## 🧠 Memory

Conversations are saved to `chat_history.txt`, allowing the assistant to remember previous interactions across sessions.

---

## 📝 Customization

You can modify the assistant’s personality or prompt in:

```python
SystemMessagePromptTemplate.from_template(
    "You are a helpful personal assistant for Manika. Be friendly and kind..."
)
```

---

## 📌 Example Prompt Code

```python
from langchain.prompts.chat import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate, MessagesPlaceholder

chat_prompt = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template("You are a helpful personal assistant for Manika."),
    MessagesPlaceholder(variable_name="history"),
    HumanMessagePromptTemplate.from_template("{input}"),
])
```

---

## 🛑 Known Issues

* Requires microphone access for voice features
* Large models may not run smoothly on low-resource systems

---

## 📃 License

MIT License — feel free to use and modify.

---

## 🙋‍♀️ Author

Built with ❤️ by **Manika**

```

---
**Screenshots of the interface**
![image](https://github.com/user-attachments/assets/d3405211-d66e-431b-97c3-6bad411208c5)

![image](https://github.com/user-attachments/assets/9066218a-1197-4a1a-80a6-e7d1cdd2c20f)



```
