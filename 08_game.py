import random

numbers = random.randint(1, 10)

while True:
    user_number = input('Enter number: ')
    user_number = int(user_number)
    if user_number == numbers:
        result = user_number
        break

print(result)

