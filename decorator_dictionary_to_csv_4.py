def format_to_csv(function):
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        if len() == 0:  # ile jest elementów, jeśli w result jest 0
            return ''   # zwraca pusty string

        keys = result[0].keys()   # jest też możliwość metody
                                # pop = popranie pierwszego elementu
                                # shift pobranie ostatniego elementu
                              # ale modyfikują liste
        output = [';'.join(keys)]  # [first_name;last_name]

        for row in
        return

    return wrapper


def test_format_to_csv():
    @format_to_csv
    def return_dict():
        return [
            {
                'first_name': 'Jacob',
                'last_name': 'Smith'
            },
            {
                'first_name': 'Emma',
                'last_name': 'Johnson'
            },
            {
                    'first_name': 'Daniel',
                    'last_name': 'Williams'
            }
        ]
    result = return_dict()

    assert result == 'first_name;last_name\nJacob;Smith\nEmma;Johnson\nDaniel;Williams\n'

# decorator notation without @
# format_to_csv(return_dict)()

