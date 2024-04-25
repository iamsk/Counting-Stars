import time
import jsonlines
from dotenv import load_dotenv

load_dotenv()
from providers.dify import dify


def save(provider):
    count = 0
    with jsonlines.open(f'results/{provider.name}_32_32.txt', mode='a') as writer:
        with jsonlines.open('Counting_Stars_Random_32_32_oversea.jsonl') as reader:
            for obj in reader:
                count += 1
                print(count)
                if count < 4:
                    continue
                dic = obj.copy()
                ret = provider.chat(obj['question'])
                dic['answer'] = ret
                writer.write(dic)
                time.sleep(15)


if __name__ == '__main__':
    save(dify)
