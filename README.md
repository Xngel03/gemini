
# 🤖 Gemini Q&A Web App

This project is an interactive web application powered by **Google's Gemini 2.0 Flash**, designed for real-time Q&A from your browser. The app combines a Python **Flask** backend with a lightweight **HTML + JavaScript frontend**, providing a clean and intelligent interface for conversational AI.

---

## 🔧 Tech Stack

- 🐍 **Python 3.10+**
- 🌐 **Flask** – Web framework for backend
- 🧠 **Gemini Flash 2.0** – Google’s powerful large language model
- 🌱 **dotenv** – Secure API key management
- 🖥️ **HTML + JavaScript** – Interactive frontend

---

## 🚀 Features

- 🔍 Ask any question in a web interface
- ⚡ Get intelligent answers from Gemini Flash 2.0
- 💬 Interactive frontend built from scratch (no frameworks)
- 🌐 REST API (`/ask`) to send and receive questions/answers

---

## 📁 Project Structure

```
gemini-qna-app/
├── app.py               # 🚀 Flask server logic and endpoints
├── gemini.py            # 🔐 Gemini integration logic (API key, prompt)
├── templates/
│   └── index.html       # 🌐 Frontend UI (form + display)
├── .env                 # 🔑 API key (do NOT share publicly)
├── requirements.txt     # 📦 Python dependencies
└── README.md            # 📘 Project instructions
```

---

## ⚙️ Setup Instructions

### 1. Clone and Navigate

```bash
git clone https://github.com/your-username/gemini-qna-app.git
cd gemini-qna-app
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
.venv\Scripts\activate   # Windows
# OR
source .venv/bin/activate  # macOS/Linux
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

### 4. Add Your Gemini API Key

Create a `.env` file in the project root:

```
GEMINI_API_KEY=your-api-key-here
```

---

## ▶️ Running the App

```bash
python app.py
```

Then open your browser and visit:

[http://127.0.0.1:5000/](http://127.0.0.1:5000/)

Ask a question and receive an AI-generated answer instantly.

---

## 🧪 Example Interaction

```
Q: What is Artificial Intelligence?
A: Artificial Intelligence (AI) is the simulation of human intelligence processes by machines.
```

---

## 👩‍💻 Developed By

**Angel Reji**  
Built with ❤️ using Flask + Gemini + HTML

---

## 📝 License

MIT License — free to use, share, and modify.
