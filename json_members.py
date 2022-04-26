from json import load, dump
with open('data.json', 'r') as data:
    course = load(data)
    #  print(course)
    print(f'Name of the course: {course["name"]}')
    print(f'Enrolled students: ')
    for member in course['members']:
        print(f'- {member["first_name"]} {member["last_name"]}')

    first_name = input('')
    last_name = input('')

    with open('data.json', 'w') as data:  # 'w' a nie 'a' bo nie dopisujemy osobnej lini tylko zamieniamy na dane z dopisaną linią
        course['members'].append({
            'id': len(course['members']) + 1,
            'first_name': first_name,
            'last_name': last_name
        })
        dump(course, data)  # przyjmuje dwa parametry (1) object (2) file pointer


