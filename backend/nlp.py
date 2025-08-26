# NLP router for chat and model logic
from flask import Blueprint, request, jsonify
import requests

nlp_router = Blueprint('nlp', __name__)


OLLAMA_URL = 'http://localhost:11434/api/generate'

# Model mapping for different tasks
MODEL_MAP = {
    'conversation': 'llama3',           # LLaMA-3 (8B or 70B)
    'coding': 'deepseek-coder',         # DeepSeek Coder
    'fast': 'mistral',                  # Mistral 7B or Phi-3 Mini
    'balanced': 'olmo2'                 # OLMo 2 (7B/13B)
}

# Helper to select model based on user input or explicit type
def select_model(user_input, mode=None):
    if mode in MODEL_MAP:
        return MODEL_MAP[mode]
    # Simple keyword-based detection for demo
    if any(word in user_input.lower() for word in ['code', 'python', 'function', 'class', 'bug', 'error']):
        return MODEL_MAP['coding']
    if any(word in user_input.lower() for word in ['quick', 'fast', 'short', 'brief']):
        return MODEL_MAP['fast']
    if any(word in user_input.lower() for word in ['balance', 'general', 'average']):
        return MODEL_MAP['balanced']
    return MODEL_MAP['conversation']

@nlp_router.route('/chat', methods=['POST'])
def chat():
    data = request.get_json(silent=True) or {}
    user_input = data.get('text', '')
    mode = data.get('mode', None)  # Optional: allow explicit mode selection
    model = select_model(user_input, mode)
    from flask import Response, stream_with_context
    payload = {
        'model': model,
        'prompt': user_input,
        'system': 'You are Stella, a helpful AI assistant. Be brief and concise, especially for greetings.',
        'stream': True
    }
    import time
    def generate():
        start_time = time.time()
        first_chunk_sent = False
        try:
            with requests.post(OLLAMA_URL, json=payload, stream=True, timeout=60) as ollama_res:
                ollama_res.raise_for_status()
                for line in ollama_res.iter_lines():
                    if line:
                        import json
                        try:
                            data = json.loads(line.decode('utf-8'))
                            chunk = data.get('response', '')
                            if chunk:
                                if not first_chunk_sent:
                                    first_chunk_sent = True
                                yield chunk
                                # If first chunk not sent within 30s, break
                                if not first_chunk_sent and (time.time() - start_time) > 30:
                                    yield "[Ollama error] Response took too long."
                                    break
                        except Exception:
                            continue
        except Exception as e:
            yield f"[Ollama error] {str(e)}"
    return Response(stream_with_context(generate()), mimetype='text/plain')
