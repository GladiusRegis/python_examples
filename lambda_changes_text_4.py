people = ['jAck shepharD', 'aNNe AUsten', 'jameS Ford']


def capitalize(word):
    return word[0].upper() + word[1:].lower()


def clean_up_names(persons: list) -> list:
    persons = map(lambda person: person.lower(), persons)
    persons = map(lambda person: person.split(' '), persons)
    persons = map(lambda person: capitalize(person[0]) + ' ' + capitalize(person[1]), persons)
    persons = sorted(persons, key=lambda person: person.split(' ')[1])
    # split rozbicie na imię i nazwisko i sortowanie po nazwisku [1]
    return list(persons)


def test_clean_up_names():
    # given
    persons = ['beN LInus', 'RichaRD AlpeRt', 'daniel FaRadaY']
    # when
    cleand = clean_up_names(persons)
    # then
    assert cleand == ['Richard Alpert', 'Daniel Faraday', 'Ben Linus']

