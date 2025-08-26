
# TTS router for text-to-speech
from flask import Blueprint, request, send_file, make_response, jsonify
import io
import tempfile
from gtts import gTTS
import os

tts_router = Blueprint('tts', __name__)



@tts_router.route('/speak', methods=['POST'])
def speak():
    text = request.json.get('text', '')
    if not text:
        return jsonify({'error': 'No text provided'}), 400
    tts = gTTS(text)
    with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as tf:
        tts.save(tf.name)
        tf.flush()
        tf.seek(0)
        audio_data = tf.read()
    response = make_response(audio_data)
    response.headers.set('Content-Type', 'audio/mpeg')
    response.headers.set('Content-Disposition', 'attachment', filename='output.mp3')
    return response
