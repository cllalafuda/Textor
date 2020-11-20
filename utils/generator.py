import mc


lst = []

with open("grob_texts.txt", encoding="utf-8") as f:
    for sent in f.read().split("\n"):
        lst.append(sent)


gen = mc.StringGenerator(samples=lst)
print(
    gen.generate_string(
        validator=mc.validators.words_count(minimal=5, maximal=10),
    )
)
