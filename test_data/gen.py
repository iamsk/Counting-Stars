import json
import random


def get_sky(sky_dir):
    sky_file = open(sky_dir, "r", encoding="utf-8")
    return '\n'.join(sky_file.readlines())


stars = [3, 5, 9, 15, 19, 21, 26, 29, 35, 38, 42, 46, 49, 54, 58, 61, 66, 69, 74, 77, 81, 86, 89, 94, 97, 102, 107, 109,
         113, 117, 122, 127, 130, 135, 139, 142, 145, 150, 153, 158, 162, 167, 171, 175, 178, 183, 185, 190, 194, 198,
         201, 206, 211, 213, 217, 223, 227, 230, 235, 239, 243, 245, 249, 255]
random.shuffle(stars)
retrieval_question = "\n\n\n\nOn this night with bright moonlight and swirling clouds, the little penguin is looking up at the sky, counting ★ intently.Please help the little penguin collect all the number of ★，example: {\"little_penguin\":[x,x,x,...]}, Do not sum, The number of stars counted by the little penguin each time in [x,x,x,...], Only output results in JSON format, no need to output any explanations."
scalar = 4.5
version = [[32, 32]]
max_context_length = 128000

if __name__ == '__main__':
    sky = get_sky("pg.txt")
    for m, n in version:
        line_count = 0
        interval = int(max_context_length / n)
        sky_size = [int(i * scalar) for i in range(interval, max_context_length + 1, interval)]
        print(sky_size)
        file_name = f"Counting_Stars_{m}_{n}.jsonl"
        test_data = open(file_name, "w", encoding="utf-8")
        for j in sky_size:
            indicator = 0
            sprinkle_stars_sky = sky[:j]
            # print(sprinkle_stars_sky)
            # exit()
            for k in range(0, j, int(j / m)):
                star_number = stars[indicator]
                indicator += 1
                single_star = f"\nLittle penguin counted {star_number} stars★\n"
                sprinkle_stars_sky = (
                        sprinkle_stars_sky[:k + int(j / m)] + single_star + sprinkle_stars_sky[k + int(j / m):])
                if indicator == m:
                    print(f"撒了{indicator}次星星")
                    break
            output_template = {
                "question": sprinkle_stars_sky + retrieval_question, "sky_size": j,
                "retrieval_question": retrieval_question,
                "reference_counting_results": stars[:m],
                "parameters": {"temperature": 0.0, "frequency_penalty": 0.0, "presence_penalty": 0.0}
            }
            print(json.dumps(output_template, ensure_ascii=False), file=test_data)
            line_count += 1
            test_data.flush()
        test_data.close()
        print(f"共计{line_count}条数据")
