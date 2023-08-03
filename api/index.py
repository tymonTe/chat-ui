from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)


class OpenAIModelID:
    GPT_3_5 = 'gpt-3.5-turbo'
    GPT_4 = 'gpt-4'
    GPT_4_32K = 'gpt-4-32k'


OpenAIModels = {
    OpenAIModelID.GPT_3_5: {
        'id': OpenAIModelID.GPT_3_5,
        'name': 'GPT-3.5',
        'maxLength': 12000,
        'tokenLimit': 4000,
    },
    OpenAIModelID.GPT_4: {
        'id': OpenAIModelID.GPT_4,
        'name': 'GPT-4',
        'maxLength': 24000,
        'tokenLimit': 8000,
    },
    OpenAIModelID.GPT_4_32K: {
        'id': OpenAIModelID.GPT_4_32K,
        'name': 'GPT-4-32K',
        'maxLength': 96000,
        'tokenLimit': 32000,
    },
}


@app.route('/api/foo')
def home():
    return 'Hello, World!'


@app.route('/api/chat')
def chat():
    return 'About'


@app.route('/api/models', methods=['POST'])
def models():
    try:
        key = request.json.get('key')
        openai.api_key = key if key else os.getenv("OPENAI_API_KEY")
        response = openai.Model.list()

        models = []
        for available_model in response['data']:
            model_name = available_model['id']
            for available_model_name, model in OpenAIModels.items():
                if available_model_name == model_name:
                    models.append({
                        'id': available_model['id'],
                        'name': model['name']
                    })

        return jsonify(models), 200
    except Exception as e:
        print(e)
        return 'Error', 500
