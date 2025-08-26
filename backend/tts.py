
# TTS router for text-to-speech
from flask import Blueprint, request, send_file, make_response, jsonify
import io
import tempfile
import pyttsx3
import os

tts_router = Blueprint('tts', __name__)

def get_engine():
    engine = pyttsx3.init()
    return engine

@tts_router.route('/voices', methods=['GET'])
def list_voices():
    engine = get_engine()
    voices_obj = engine.getProperty('voices')
    voices = []
    if isinstance(voices_obj, (list, tuple)):
        voices = list(voices_obj)
    voices_list = []
    for v in voices:
        lang = ''
        if v.languages:
            lang_val = v.languages[0]
            if isinstance(lang_val, bytes):
                lang = lang_val.decode()
            else:
                lang = str(lang_val)
        voices_list.append({
            'id': v.id,
            'name': v.name,
            'gender': getattr(v, 'gender', ''),
            'lang': lang
        })
    return jsonify({'voices': voices_list})

@tts_router.route('/speak', methods=['POST'])
def speak():
    data = request.get_json(silent=True) or {}
    text = data.get('text', '')
    # Always use Zira (female) as the default voice
    zira_id = "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-US_ZIRA_11.0"
    voice_id = data.get('voice_id', zira_id)
    engine = get_engine()
    engine.setProperty('voice', voice_id)
    import logging
    logging.basicConfig(level=logging.DEBUG)
    with tempfile.NamedTemporaryFile(delete=False, suffix='.wav') as tf:
        temp_path = tf.name
    try:
        logging.debug(f"[TTS] Saving to: {temp_path}")
        engine.save_to_file(text, temp_path)
        engine.runAndWait()
        file_exists = os.path.exists(temp_path)
        file_size = os.path.getsize(temp_path) if file_exists else 0
        logging.debug(f"[TTS] File exists: {file_exists}, Size: {file_size} bytes")
        if not file_exists or file_size == 0:
            logging.error(f"[TTS] Audio file not created or empty!")
            return make_response('TTS error: file not created', 500)
        with open(temp_path, 'rb') as f:
            audio_data = f.read()
        logging.debug(f"[TTS] Read {len(audio_data)} bytes from file.")
        response = make_response(audio_data)
        response.headers['Content-Type'] = 'audio/wav'
        return response
    finally:
        if os.path.exists(temp_path):
            os.remove(temp_path)
