list_2 = ['cat', 'horse', 'squirrel', 'beaver', 'butterfly']


def filter_words(words: list) -> list:
    return [word for word in words if 4 < len(word) < 8]


print(filter_words(list_2))
