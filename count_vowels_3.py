def count_vowels(text):
    return sum([char in 'aeouy' for char in text])


print(count_vowels('ala'))

print(count_vowels('programowanie'))