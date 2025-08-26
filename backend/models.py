# Models router for model selection and info
from flask import Blueprint, request, jsonify

models_router = Blueprint('models', __name__)

@models_router.route('/list', methods=['GET'])
def list_models():
    # Placeholder: return dummy model list
    return jsonify({'models': ['llama3', 'deepseek-coder', 'mistral', 'phi3', 'olmo2']})

@models_router.route('/select', methods=['POST'])
def select_model():
    data = request.get_json(silent=True) or {}
    model = data.get('model', 'llama3')
    # Placeholder: pretend to select model
    return jsonify({'selected': model})
