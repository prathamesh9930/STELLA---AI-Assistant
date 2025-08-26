# Stella AI Backend (Flask)
# Entry point for the assistant backend

from flask import Flask, request, jsonify, send_file, render_template
from backend.nlp import nlp_router
from backend.tts import tts_router
from backend.stt import stt_router
from backend.memory import memory_router
from backend.system import system_router
from backend.models import models_router
from backend.vscode import vscode_router
import os

app = Flask(__name__, template_folder='templates')

# Register blueprints (modular routers)
app.register_blueprint(nlp_router, url_prefix='/api/nlp')
app.register_blueprint(tts_router, url_prefix='/api/tts')
app.register_blueprint(stt_router, url_prefix='/api/stt')
app.register_blueprint(memory_router, url_prefix='/api/memory')
app.register_blueprint(system_router, url_prefix='/api/system')
app.register_blueprint(models_router, url_prefix='/api/models')

app.register_blueprint(vscode_router, url_prefix='/api/vscode')

@app.route('/')
def index():
    return render_template('jarvis.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
