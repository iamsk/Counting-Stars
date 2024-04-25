import os
import json
from dify_client import ChatClient


class Base(object):
    def __init__(self, api_key):
        self.name = self.api_key = api_key

    def chat(self, query):
        chat_client = ChatClient(self.api_key)
        chat_response = chat_client.create_chat_message(inputs={}, query=query, user="Counting-Stars",
                                                        response_mode="blocking")
        chat_response.raise_for_status()
        content = chat_response.json()['answer']
        return content.replace('```json', '```').replace('```', '').replace("\n", '')

    def chat_stream(self, query):
        chat_client = ChatClient(self.api_key)
        chat_response = chat_client.create_chat_message(inputs={}, query=query, user="Counting-Stars",
                                                        response_mode="streaming")
        content = ''
        for line in chat_response.iter_lines(decode_unicode=True):
            print(line)
            if not line.startswith('data:'):
                continue
            line = line.split('data:', 1)[-1]
            if line.strip():
                line = json.loads(line.strip())
                content += line.get('answer')
        return content.replace('```json', '```').replace('```', '').replace("\n", '')


dify = Base(os.getenv('DIFY_APP_KEY'))
