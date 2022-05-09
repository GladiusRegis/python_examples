states_of_america = {
    'Alabama': 'Montgomery',
    'Alaska': 'Juneau',
    'Arizona': 'Phoenix',
    'Arkansas': 'Little Rock'
}


try:
    state = input('Enter us state name: ')
    print(states_of_america[state])

except KeyError:
    print(f'Enter a valid state name, there is no {state} state')
