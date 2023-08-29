# Task 1
hp = int(input('Enter hp number: '))
if hp > 0:
    alive = True
else:
    alive = False
print(alive)


# Task 2
number = int(input('Enter the number: '))
if number%2 == 0:
    print("Чётное")
else:
    print("Нечётное")


# Task 3
year = int(input('Enter the year: '))
if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
    print("Високосный год")
else:
    print("Год не високосный")

# Task 4
text = input('Enter the text: ')
prints = int(input('How many times to print the text: '))
for i in range(1, prints + 1):
    print(text)


# Task 5
exp = input('Enter the mathematical expression: ')
print(eval(exp))