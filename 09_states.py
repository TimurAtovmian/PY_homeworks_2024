states = {
    'CZ': 'Česko',
    'SK': 'Slovensko',
    'PL': 'Polsko',
    'DE': 'Německo',
    'AT': 'Rakousko',
}

states['HU'] = 'Madarsko'

states_length = {}

for key, value in states.items():
    states_length[key] = len(value)

print(states_length)