def count_vowels(text):
    return sum([char in 'aeouy' for char in text])
    # returns true false


# Kacper way
def count_vowels2(text):
    return sum([1 if char in 'aeouy' else 0 for char in text])


print(count_vowels('ala'))
print(count_vowels('lll'))
print(count_vowels('programing'))

print(count_vowels2('ala'))
print(count_vowels2('lll'))
print(count_vowels2('programing'))
