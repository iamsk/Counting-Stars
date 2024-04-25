import os
from zhipuai import ZhipuAI

client = ZhipuAI(api_key=os.getenv('ZHIPU_API_KEY'))


class Zhipu(object):
    name = '智谱'

    @staticmethod
    def chat(prompt):
        messages = [
            {"role": "user", "content": prompt},
        ]
        completion = client.chat.completions.create(
            model="glm-4",
            messages=messages,
            temperature=0.01,
            max_tokens=1999,
        )
        return completion.choices[0].message.content


zhipu = Zhipu()
