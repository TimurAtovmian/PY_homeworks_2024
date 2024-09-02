numbers = [-98, 23, 27, 91, -46, -26, -69, -53, -62, -93, 17, 50, -65, 18, -38, -4, 75, -79, -98, -56, -57, 89]

number_of_positiv_numbers = 0
number_of_negative_numbers = 0

for number in numbers:
    if number < 0:
        number_of_negative_numbers += 1
    elif number > 1:
        number_of_positiv_numbers += 1

print("Number of negativ numbers:", number_of_negative_numbers)
print("Number of positive numbers:", number_of_positiv_numbers)