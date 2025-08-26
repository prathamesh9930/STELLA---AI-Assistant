# System router for system commands
from flask import Blueprint, request, jsonify

system_router = Blueprint('system', __name__)

@system_router.route('/command', methods=['POST'])
def command():
    data = request.get_json(silent=True) or {}
    cmd = data.get('cmd', '')
    # Placeholder: do not run real commands
    return jsonify({'result': f'Pretend to run: {cmd}'})
