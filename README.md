# Enhanced LLM Agent (POC)

An interactive **web-based chat agent** that integrates with multiple LLM providers (OpenAI, Google Gemini, AI Pipe Proxy, and Mock) and offers a developer-friendly sandbox for testing responses, code execution, and API integrations.

---

## 🚀 Features

- **Multi-Provider Support**
  - OpenAI GPT models
  - Google Gemini
  - AI Pipe Proxy (custom LLM backend)
  - Local Mock provider (for testing without API keys)

- **Modern Chat UI**
  - Chat bubbles with avatars & timestamps
  - Typing indicators
  - Message streaming simulation
  - Code blocks with syntax highlighting and copy button

- **Configurable API Keys**
  - Stored in `localStorage` for convenience
  - Add/remove keys via the right-side panel

- **Built-in Sandbox**
  - Execute JavaScript safely within the browser

---

## ⚙️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Shreya-agr09/ppt-generator.git
   cd ppt-generator
   
2. **Set up virtual env**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate ```
   
3. **Installing dependencies**
   ```pip install -r requirements.txt ```

## 🚀 Usage

### Running locally (FastAPI with Uvicorn)

```bash uvicorn app:app --reload```

### Running with ngrok

#### 1.Add your ngrok auth token:
```bash ngrok config add-authtoken <YOUR_AUTH_TOKEN>```
#### 2.Update app.py with your reserved domain (if any).

#### 3.Start the app:
   ```bash python app.py```
   
## 📡 API Endpoints

- **`GET /`** → Landing page with chat UI.  
- **`POST /generate`** → Generate responses from the selected provider.  
- **`POST /sandbox`** → Execute sandboxed JavaScript code.  

---

## 🎨 Templates

- All Jinja2 HTML templates are stored in the **`templates/`** directory.  
- Static assets (CSS, JS) are located in the **`static/`** directory.  

---

## 👩‍💻 Development

- **Frontend:** HTML + Bootstrap + custom JS  
- **Backend:** FastAPI + Python  
- **Presentation:** PowerPoint generation using `python-pptx`  

---

## 🔒 Security Notes

- API keys are stored locally (browser `localStorage`).  
- Sandbox executes **client-side only** code.  
- Never expose production API keys in the repo.  

