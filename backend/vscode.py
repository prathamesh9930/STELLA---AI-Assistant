# VS Code control utilities for Stella AI
import subprocess
import os
from flask import Blueprint, request, jsonify

vscode_router = Blueprint('vscode', __name__)

@vscode_router.route('/open', methods=['POST'])
def open_in_vscode():
    data = request.get_json(silent=True) or {}
    path = data.get('path')
    if not path:
        return jsonify({'error': 'No path provided'}), 400
    try:
        # Use code.cmd for Windows
        subprocess.Popen(['code', path], shell=True)
        return jsonify({'result': f'Opened {path} in VS Code'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@vscode_router.route('/edit', methods=['POST'])
def edit_file():
    data = request.get_json(silent=True) or {}
    path = data.get('path')
    content = data.get('content')
    if not path or content is None:
        return jsonify({'error': 'Path and content required'}), 400
    try:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        return jsonify({'result': f'Edited {path}'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@vscode_router.route('/run', methods=['POST'])
def run_code():
    data = request.get_json(silent=True) or {}
    path = data.get('path')
    if not path:
        return jsonify({'error': 'No path provided'}), 400
    ext = os.path.splitext(path)[1]
    try:
        if ext == '.py':
            result = subprocess.check_output(['python', path], stderr=subprocess.STDOUT, shell=True, encoding='utf-8')
        elif ext == '.js':
            result = subprocess.check_output(['node', path], stderr=subprocess.STDOUT, shell=True, encoding='utf-8')
        else:
            return jsonify({'error': 'Unsupported file type'}), 400
        return jsonify({'output': result})
    except subprocess.CalledProcessError as e:
        return jsonify({'output': e.output, 'error': str(e)})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
