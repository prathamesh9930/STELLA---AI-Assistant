# STT router for speech-to-text
from flask import Blueprint, request, jsonify

stt_router = Blueprint('stt', __name__)

@stt_router.route('/listen', methods=['POST'])
def listen():
    # Placeholder: return dummy transcript
    return jsonify({'transcript': 'This is a dummy transcript.'})
