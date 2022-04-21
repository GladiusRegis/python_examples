def format_to_csv(function):
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        if len(result) == 0:
            return ''

        keys = result[0].keys()
        output = [';'.join(keys)]  # [first_name;last_name]

        for row in result:
            row_list = str(row.values())
            output.append(';'.join(row_list))  # ['Jacob;Smith','...']
        return '\n'.join(output)

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

    assert result == 'first_name;last_name\nJacob;Smith\nEmma;Johnson\nDaniel;Williams'

# decorator notation without @
# format_to_csv(return_dict)()

@format_to_csv
def return_sample():
    return [
        {'id': 1, 'name': 'lemon'},
        {'id': 2, 'name': 'orange'},
        {'id': 3, 'name': 'pineapple'}
    ]


print(return_sample())
