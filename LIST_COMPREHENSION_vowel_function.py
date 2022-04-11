def choose_vowels2(words):

    vowels_set = set()
    for char in words.lower():
        if char in 'aeiouy':
            vowels_set.add(char)
    return vowels_set


print(choose_vowels2(input('text:')))


def choose_vowels1(words):
    return {char for char in words.lower() if char in 'aeiouy'}


print(choose_vowels1(input('text:')))
