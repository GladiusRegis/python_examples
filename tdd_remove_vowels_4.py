def remove_vowels(text: str) -> str:
    for char in text:
        if char in 'aeiouyAEIOUY':
            text = text.replace(char, '')
    return text


def test_vowels_none():
    assert remove_vowels('this is Sparta') == 'ths s Sprt'
    assert remove_vowels('Arkadius Ursa') == 'rkds rs'
