content = input('Enter the text to reverse: ')
try:
    if content == '':
        raise ValueError('The text was not given!')

    print(content[::-1])
except ValueError as error:
    print(error)
