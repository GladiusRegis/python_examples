def return_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowels_set = set()
    for vowel in vowels:
        for cher in text:
            if cher == vowel:
                vowels_set.add(vowel)
    return vowels_set


print(return_vowels(input('text:')))
