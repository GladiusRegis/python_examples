def choose_vowels2(words):

    vowels_set = set()
    for char in words.lower():
        if char in 'aeiouy':
            vowels_set.add(char)
    return vowels_set


print(choose_vowels2(input('text:')))



