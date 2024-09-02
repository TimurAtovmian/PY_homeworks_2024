name = input('Enter your name: ')
age = input('Enter your age: ')
age = int(age)

cesta = 'PY_homeworks_2024\02_user.txt'

with open(cesta, mode = 'w') as file:
    file.write(f'Name: {name}, Age: {age}')