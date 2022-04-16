
def count_letters(text, start='(', end=')'):
    should_count = False
    counter = 0
    temp_counter = 0
    for char in text:
        if char == end:
            should_count = False
            counter += temp_counter
            temp_counter = 0

        if should_count:
            temp_counter += 1

        if char == start:
            should_count = True

    return counter


def test_none_end():
    assert count_letters('what (is this') == 0
    assert count_letters('what (is this)') == 7


def test_count_letters_once():
    assert count_letters('what (is) this') == 2


def test_letters_none():
    assert count_letters('what is this') == 0
    assert count_letters('what (is) this', '<', '>') == 0


def test_multiple_brackets():
    assert count_letters('what (is) (this)') == 6
    assert count_letters('what <is> <this>', '<', '>') == 6


