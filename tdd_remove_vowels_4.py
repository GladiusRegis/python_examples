def remove_vowels1(text) -> str:
    vowels = 'aeiouyAEIOUY'
    text = str(text)
    for char in text:
        if char in vowels:
            text = text.replace(char, '')
    return text


def remove_vowels2(text) -> str:
    vowels = 'aeiouyAEIOUY'
    for char in str(text):
        if char in vowels:
            text = text.replace(char, '')
    return text
# error when casting a variable in a loop


def remove_vowels3(text) -> str:
    vowels = 'aeiouyAEIOUY'
    #  return ''.join([text.replace(char, '') for char in str(text) if char in vowels])
    # the list comprehension doesn't work
    return ''.join([char for char in str(text) if char not in vowels])


def remove_vowels4(text: str) -> str:
    vowels = 'aeiouyAEIOUY'
    result = ''
    for char in str(text):
        if char not in vowels:
            result += char
    return result


def remove_vowels5(text: str) -> str:
    vowels = 'aeiouyAEIOUY'
    return ''.join([char for char in str(text) if char not in vowels])


def test_remove_vowels1():
    assert remove_vowels1('this is Sparta') == 'ths s Sprt'
    assert remove_vowels1('Arkadius Ursa') == 'rkds rs'
    assert remove_vowels1('') == ''
    assert remove_vowels1(12345) == '12345'


def test_remove_vowels2():
    assert remove_vowels2('this is Sparta') == 'ths s Sprt'
    assert remove_vowels2('Arkadius Ursa') == 'rkds rs'
    assert remove_vowels2('') == ''
    assert remove_vowels2(12345) == '12345'


def test_remove_vowels3():
    assert remove_vowels3('this is Sparta') == 'ths s Sprt'
    assert remove_vowels3('Arkadius Ursa') == 'rkds rs'
    assert remove_vowels3('') == ''
    assert remove_vowels3(12345) == '12345'


def test_remove_vowels4():
    assert remove_vowels4('this is Sparta') == 'ths s Sprt'
    assert remove_vowels4('Arkadius Ursa') == 'rkds rs'
    assert remove_vowels4('') == ''
    assert remove_vowels4(12345) == '12345'


def test_remove_vowels5():
    assert remove_vowels5('this is Sparta') == 'ths s Sprt'
    assert remove_vowels5('Arkadius Ursa') == 'rkds rs'
    assert remove_vowels5('') == ''
    assert remove_vowels5(12345) == '12345'
