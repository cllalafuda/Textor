import mc
import random


def normalize_data(data) -> str:
    """
    уменьшает количество символов для корректной
    и быстрой работы генератора
    """
    if len(data) > 318775:  # примерное количество символов
        idx = random.randint(0, len(data) - 318775)
        data = data[idx:idx + 318775]

    return data


def get_data(name, database) -> str:
    result = database.get_data_for_generating(name)
    return result


def generate_lyrics(is_song: bool, templates: list, database) -> str:
    data_for_generator = []

    for name in templates:
        data = normalize_data(get_data(name, database)).split("\n")
        data_for_generator.extend(data)

    chorus = None

    try:
        gen = mc.StringGenerator(samples=data_for_generator)
    except ValueError:
        return ""

    if is_song:
        chorus = "Припев:\n" + "\n".join([generate_string(gen) for _ in range(4)])

    couplets = []
    strings_count = int(random.randint(1, 3))

    couplet_strings_count = random.randint(4, 6)
    for _ in range(strings_count):
        couplet = "\n".join(
            [generate_string(gen).capitalize() for _ in range(couplet_strings_count)]
        )
        couplets.append(couplet)

        if chorus is not None:
            couplets.append(chorus)

    result = "\n\n".join(couplets)
    return result


def generate_string(gen) -> str:
    string = None

    while string is None:
        string = gen.generate_string(
            validator=mc.validators.words_count(minimal=5, maximal=10),
        )

    return string
