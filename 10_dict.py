ceny_potravin = {
    'máslo': 30,
    'chleba': 20,
    'sýr': 30,
    'jablko': 5
}

ceny_potravin['Mleko'] = 25

min_key = ''
min_value = 100_000

for key, value in ceny_potravin.items():
    if min_value > value:
        min_key = key
        min_value = value

print(min_key, min_value)


     

