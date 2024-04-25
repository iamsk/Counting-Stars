import os
import requests


class Xverse(object):
    name = '元象大模型'

    @staticmethod
    def chat(prompt):
        messages = [
            {"role": "user", "content": prompt},
        ]
        api_key = os.getenv('XVERSE_API_KEY')
        headers = {
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/json',
        }
        json_data = {
            'messages': messages,
            'plugin': 'MODEL',
            'model': 'XVERSE-13B-LONGCONTEXT',
            'temperature': 0.01,
            'max_tokens': 1999
        }
        response = requests.post('https://api.xverse.cn/v1/chat/completions', headers=headers, json=json_data)
        return response.json()['choices'][0]['message']['content']


xverse = Xverse()
