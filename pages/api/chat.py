from http.server import BaseHTTPRequestHandler
import json
from tiktoken import Tokenizer
from tiktoken.models import Model

from utils.app.consts import DEFAULT_SYSTEM_PROMPT, DEFAULT_TEMPERATURE


class handler(BaseHTTPRequestHandler):

    def do_POST(self):
        try:
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data)

            model = data.get('model')
            messages = data.get('messages')
            key = data.get('key')
            prompt = data.get('prompt', DEFAULT_SYSTEM_PROMPT)
            temperature = data.get('temperature', DEFAULT_TEMPERATURE)

            tokenizer = Tokenizer()
            model = Model()

            prompt_tokens = tokenizer.encode(prompt)
            token_count = len(prompt_tokens)

            messages_to_send = []

            for message in reversed(messages):
                tokens = tokenizer.encode(message.get('content'))
                if token_count + len(tokens) + 1000 > model.token_limit:
                    break
                token_count += len(tokens)
                messages_to_send.insert(0, message)

            # OpenAIStream function is not available in Python. You have to implement it yourself or find a Python equivalent.

            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(json.dumps({"stream": "OpenAIStream response"}).encode())
        except Exception as e:
            print(e)
            self.send_response(500)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(str(e).encode())
        return
