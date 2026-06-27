# ✨ Mishi AI — Intelligent Conversation Partner

![Mishi AI](https://img.shields.io/badge/Mishi-AI-a78bfa?style=for-the-badge&logo=sparkles)
![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.35+-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Gemini](https://img.shields.io/badge/Gemini-2.5_Flash-4285F4?style=for-the-badge&logo=google&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

> A sleek, dark-themed AI chatbot powered by **Google Gemini 2.5 Flash**, built with Streamlit. Features smooth animations, a persistent sidebar, recent chat history, and a polished purple UI.

---

## 🚀 Features

- 💬 Real-time chat powered by Google Gemini 2.5 Flash
- ✨ Animated thinking indicator with pulse & slide effects
- 🎨 Dark purple-themed UI with smooth message animations
- 📋 Recent chat history in the sidebar
- 💡 Suggestion prompts on the welcome screen
- 🔗 GitHub & LinkedIn profile links
- 📱 Wide layout, responsive design

---

## 🗂️ Project Structure

```
MishiAI/
├── ChatBot.py           # Main Streamlit app
├── requirements.txt     # Python dependencies
├── .gitignore           # Git ignored files
├── LICENSE              # MIT License
└── README.md            # This file
```

---

## ⚙️ Local Setup

### 1. Clone the repository
```bash
git clone https://github.com/Mrj086/MishiAIchatbot.git
cd MishiAIchatbot
```

### 2. Create a virtual environment (recommended)
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Add your Gemini API key

Create the Streamlit secrets folder and file:
```bash
mkdir -p .streamlit
```

Create `.streamlit/secrets.toml` and add:
```toml
GEMINI_API_KEY = "your-gemini-api-key-here"
```

> 🔑 Get your free API key at: https://aistudio.google.com/app/apikey

### 5. Run the app locally
```bash
streamlit run ChatBot.py
```

Open your browser at `http://localhost:8501`

---

## ☁️ Deploy on Streamlit Community Cloud (Free)

### Step 1 — Push your code to GitHub

Make sure your repo has these files:
```
ChatBot.py
requirements.txt
.gitignore
README.md
```

> ⚠️ Do NOT push `.streamlit/secrets.toml` — it's in `.gitignore` for security.

```bash
git add ChatBot.py requirements.txt .gitignore README.md LICENSE
git commit -m "Initial commit"
git push origin main
```

---

### Step 2 — Sign in to Streamlit Cloud

Go to 👉 [https://share.streamlit.io](https://share.streamlit.io)

Sign in with your **GitHub account**.

---

### Step 3 — Create a new app

1. Click **"New app"**
2. Select your repository: `Mrj086/MishiAIchatbot`
3. Set the branch: `main`
4. Set the main file path: `ChatBot.py`
5. Click **"Advanced settings"** (important — see Step 4 below)

---

### Step 4 — Add your API key as a Secret

In the **Advanced settings** panel:

1. Click **"Secrets"**
2. Paste the following:

```toml
GEMINI_API_KEY = "your-gemini-api-key-here"
```

3. Click **Save**

> This is the equivalent of your local `.streamlit/secrets.toml` — Streamlit Cloud stores it securely.

---

### Step 5 — Deploy!

Click **"Deploy!"** and wait 1–2 minutes.

Your app will be live at:
```
https://your-app-name.streamlit.app
```

---

## 🔑 Getting a Gemini API Key

1. Go to [https://aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey)
2. Sign in with your Google account
3. Click **"Create API Key"**
4. Copy the key and paste it into your secrets (local or Streamlit Cloud)

> The free tier of Gemini API is generous and more than enough for personal projects.

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| [Streamlit](https://streamlit.io) | Web app framework |
| [Google Gemini 2.5 Flash](https://deepmind.google/technologies/gemini/) | AI language model |
| [google-genai](https://pypi.org/project/google-genai/) | Gemini Python SDK |
| CSS Animations | Smooth UI transitions |

---

## 🤝 Connect

- 🐙 GitHub: [Mrj086](https://github.com/Mrj086/MishiAIchatbot)
- 💼 LinkedIn: [Md. Miraj Ul Islam](https://www.linkedin.com/in/md-miraj-ul-islam-77b30b26a/)

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.
