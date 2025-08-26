# Stella AI



## 🚀 Overview
Stella AI is a modular, local AI assistant with a beautiful, futuristic UI inspired by sci-fi interfaces. It features voice interaction, memory, system integration, and multi-model support, all running locally for privacy and speed. Stella AI is optimized for both desktop and mobile, providing a seamless, visually stunning experience across devices.

---

## ✨ Features
- **Modular Flask Backend**: Clean, extensible Python backend with blueprints for NLP, TTS, STT, memory, and system integration.
- **Ollama LLM Integration**: Local LLM inference with support for multiple models (Llama3, DeepSeek Coder, Mistral, Olmo2, etc.).
- **Voice Interaction**: Local TTS (pyttsx3) and STT for hands-free operation.
- **Streaming Responses**: Fast, incremental chat streaming for a natural conversation flow.
- **Mobile-First UI**: Responsive design with a compact, scrollable chat card, sticky SVG reactor, and touch-optimized controls.
- **Model Selection**: Easily switch between models; mobile defaults to the fastest (Mistral).
- **Dynamic Estimated Response Time**: Shows real-time, model-based ETA for each response.
- **Pause/Resume**: Instantly pause or resume both streaming and vocal responses.
- **VS Code Integration**: (Desktop) Open and edit files directly from the chat.
- **Customizable Starfield Background**: Immersive, animated galaxy background for a sci-fi feel.

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

## ⚡ Quick Start
1. **Clone the repo:**
   ```sh
   git clone <your-repo-url>
   cd "Stella AI"
   ```
2. **Create a virtual environment:**
   ```sh
   python -m venv venv
   venv\Scripts\activate  # On Windows
   # Or: source venv/bin/activate  # On Mac/Linux
   ```
3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
4. **Start Ollama server:**
   ```sh
   ollama serve
   # Or to run a specific model:
   ollama run mistral
   ```
5. **Run the Flask backend:**
   ```sh
   python -m backend.app
   ```
6. **Open in your browser:**
   - Desktop: http://localhost:5000
   - Mobile: Scan your local IP with your phone

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
