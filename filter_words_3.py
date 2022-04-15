list_2 = ['cat', 'horse', 'squirrel', 'beaver', 'butterfly']


def give_words(list_words: list) -> list:
    return [word for word in list_words if 4 < len(word) < 8]


print(give_words(list_2))