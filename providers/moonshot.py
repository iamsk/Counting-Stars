import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv('MOONSHOT_API_KEY'),
    base_url="https://api.moonshot.cn/v1",
)


class Moonshot(object):
    name = 'MoonShot'

    @staticmethod
    def chat(prompt):
        messages = [
            {"role": "user", "content": prompt},
        ]
        completion = client.chat.completions.create(
            model="moonshot-v1-128k",
            messages=messages,
            temperature=0.01,
            max_tokens=1999,
        )
        return completion.choices[0].message.content


moonshot = Moonshot()
