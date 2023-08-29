# Task 1
a = int(input('Enter the number: '))
for i in range(1, a+1):
    if (i == 1) or (i == a):
        print("*"*a)
    else:
        print("*"+' '*(a-2)+"*")

# Task 2
a = input('Enter the number: ')

print("Тысячи -", a[0])
print("Сотни -", a[1])
print("Десятки -", a[2])
print("Единицы -", a[3])