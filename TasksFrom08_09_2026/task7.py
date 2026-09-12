from faker import Faker


top_words: dict[str, int] = {}


with open("TasksFrom08_09_2026/task7.txt") as f:
    for i in f:
        for symb in ",!?:;.":
            i = i.replace(symb, "")
        words = i.lower().split()
        for word in words:
            if word in top_words.keys():
                top_words[word] += 1
            else:
                top_words[word] = 1


def top_10(top_words):
    return sorted(top_words.items(), key=lambda x: x[1], reverse=True)[:10]


top = top_10(top_words)

for word, count in top:
    print(word, count)

def create_10k_words():
    fake = Faker("ru_RU")

    with open("task7_faker.txt", "w") as f:
        for _ in range(10000):
            words = f"{fake.name()} живет в городе {fake.city()} и сегодня {fake.word()} {fake.word()} {fake.word()}."

            f.write(words + "\n")


create_10k_words()
