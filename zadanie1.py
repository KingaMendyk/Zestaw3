# Zadanie 1

numbers = input("Podaj liczby rozdzielone przecinkiem: ")
number_list = numbers.split(",")

for i in range(len(number_list)):
    number_list[i] = int(number_list[i])

maximum = number_list[0]
minimum = number_list[0]
for number in number_list:
    if number > maximum:
        maximum = number
    if number < minimum:
        minimum = number

print("Max:", maximum)
print("Min:", minimum)
