# Memory router for conversation history
from flask import Blueprint, request, jsonify

memory_router = Blueprint('memory', __name__)

@memory_router.route('/history', methods=['GET', 'POST'])
def history():
    # Placeholder: return dummy history
    return jsonify({'history': ['Hi', 'Hello', 'How can I help?']})
