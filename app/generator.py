import mc
import random


lst = []

with open("../grob_texts.txt", encoding="utf-8") as f:
    for sent in f.read().split("\n"):
        lst.append(sent)

gen = mc.StringGenerator(samples=lst)


def generate_string() -> str:
    string = gen.generate_string(
        validator=mc.validators.words_count(minimal=5, maximal=10),
    )

    return string


# def generate_lyrics() -> str:
#     strings_count = int(random.choice(range(4, 17, 4)))
#     for _ in range(strings_count):
#         string = generate_string()
#         while str