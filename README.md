

# Stella AI Assistant

<p align="center">
	<img src="https://img.shields.io/badge/LLM%20Engine-Ollama-4B275F?style=for-the-badge&logo=ollama&logoColor=white" alt="Ollama"/>
	<img src="https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
	<img src="https://img.shields.io/badge/Flask-Backend-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask"/>
	<img src="https://img.shields.io/badge/Frontend-HTML5%20%7C%20CSS3%20%7C%20JS-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="Frontend"/>
	<img src="https://img.shields.io/badge/LLMs-Llama3%20%7C%20Mistral%20%7C%20DeepSeek%20Coder%20%7C%20Olmo2-6A5ACD?style=for-the-badge" alt="LLMs"/>
	<img src="https://img.shields.io/badge/Voice-TTS%20(gTTS%20%7C%20pyttsx3)%20%7C%20STT%20(Vosk)-FF69B4?style=for-the-badge" alt="Voice"/>
</p>

<div align="center" style="margin-bottom: 1em;">
	<img src="https://skillicons.dev/icons?i=python,flask,html,css,js,git" alt="Tech stack"/>
</div>









## 🚀 Overview
**Stella AI** is a modular, local AI assistant with a beautiful, futuristic UI inspired by sci-fi interfaces. It features voice interaction, memory, system integration, and multi-model support, all running locally for privacy and speed. Stella AI is optimized for both desktop and mobile, providing a seamless, visually stunning experience across devices.

---

## 🖥️ Local Requirements

- **Python 3.11+** (recommended)
- **Ollama** (for local LLMs, e.g. Llama3, Mistral, DeepSeek Coder, Olmo2)
- **Git**
- **pip** (Python package manager)
- **(Optional) VS Code** for development

### Python dependencies (auto-installed):
- torch
- transformers
- scikit-learn
- numpy
- pandas
- flask
- pyautogui
- vosk
- pyttsx3
- gTTS

See `requirements.txt` for the full list.

---

---

## 🖥️ Languages, Frameworks & Technologies
- **Languages:** Python, JavaScript, HTML, CSS
- **Frameworks/Libraries:** Flask, PyTorch, Hugging Face Transformers, pyttsx3, Vosk, Ollama
- **Frontend:** Custom HTML/CSS/JS, SVG, responsive design
- **Other:** Render.com (deployment), Git, VS Code

---

---


## ✨ Features
- Modular Flask backend (NLP, TTS, STT, memory, system integration)
- Ollama LLM integration (Llama3, DeepSeek Coder, Mistral, Olmo2, etc.)
- Local TTS (pyttsx3) and STT (Vosk)
- Streaming chat responses
- Model selection (desktop/mobile optimized)
- Dynamic ETA for responses
- Pause/resume streaming and voice
- VS Code integration (desktop)
- Customizable starfield background
- **Mobile:** Touch-optimized, compact chat card, sticky SVG reactor, and more

---

## 📱 <span id="mobile-features"></span>Mobile Features
- **Tap the red dot** (microphone) to speak to Stella (voice input)
- **Compact chat card**: Scrollable, fixed max-height for easy reading
- **Pause/Play**: Small SVG icon beside send button to pause/resume voice
- **ETA**: See estimated response time at the top-right of chat card
- **Model selection**: Defaults to fastest (Mistral) for best mobile experience
- **Starfield background**: Full viewport, immersive sci-fi look

---

---

## 📱 Mobile vs 🖥️ Desktop
| Feature                | Desktop                                      | Mobile                                         |
|------------------------|----------------------------------------------|------------------------------------------------|
| Layout                 | Wide, multi-column, large reactor            | Vertical, compact, reactor at top              |
| Chat Card              | Large, grows with content                    | Small, scrollable, fixed max-height            |
| Input Row              | Full-width, mic, model select, send          | Compact, upward arrow, pause/play beside send  |
| Pause/Play             | Not shown                                   | Small SVG icon beside send                     |
| Thinking State         | Separate overlay card                        | In-chat log, replaced by response              |
| ETA Display            | Not shown                                   | Top-right of chat card                         |
| Model Selection        | User choice, default: Mistral                | Default: Mistral (Fastest)                     |
| VS Code Integration    | Available                                   | Not available                                  |
| Background             | Starfield, full viewport                     | Starfield, full viewport                       |

---

## 🛠️ Project Structure
```
Stella AI/
├── backend/
│   ├── app.py           # Main Flask app
│   ├── nlp.py           # NLP/LLM integration (Ollama)
│   ├── tts.py           # Text-to-speech
│   ├── stt.py           # Speech-to-text
│   ├── memory.py        # Memory module
│   ├── system.py        # System integration
│   ├── vscode.py        # VS Code integration (desktop)
│   ├── models.py        # Model management
│   └── templates/
│       └── jarvis.html  # Main UI (desktop & mobile)
├── requirements.txt     # Python dependencies
├── README.md            # Project documentation
```

---


## ⚡ How to Run Locally

### 1. Clone the repository
```sh
git clone https://github.com/prathamesh9930/STELLA---AI-Assistant.git
cd "Stella AI"
```

### 2. Create and activate a virtual environment
```sh
python -m venv venv
venv\Scripts\activate  # On Windows
# Or: source venv/bin/activate  # On Mac/Linux
```

### 3. Install Python dependencies
```sh
pip install -r requirements.txt
```

### 4. Install and start Ollama (for LLMs)
- Download and install Ollama from: https://ollama.com/download
- Start the Ollama server:
```sh
ollama serve
# Or to run a specific model:
ollama run mistral
```

### 5. Run the Flask backend
```sh
python -m backend.app
```

### 6. Open Stella AI in your browser
- Desktop: http://localhost:5000
- Mobile: Open the same address on your phone (ensure both devices are on the same network)

---

---

## 🧠 Model Support
- **Llama3 (General)**
- **DeepSeek Coder (Coding)**
- **Mistral (Fast, default on mobile)**
- **Olmo2 (Balanced)**

You can add more models via Ollama and update the backend as needed.

---

## 🎨 Customization
- **Background:** Change the starfield image in `jarvis.html` for a new look.
- **UI:** Tweak CSS for colors, layout, and effects.
- **Models:** Add or remove models in the backend and UI.

---

## 🛡️ Privacy & Local-First
All AI inference, voice, and data processing happens locally. No cloud required. Your data stays on your machine.

---

## 📄 License
MIT License. See [LICENSE](LICENSE) for details.

---

## 👨‍💻 Author
- Designed & developed by Prathamesh
- With help from GitHub Copilot

---

> "Stella, initialize!" — Your local AI, always ready.
