# Task 1
my_list = ['a', 'b', [1, 2, 3], 'd']
print(my_list[2])

# Task 2
list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
my_sum = 0
a_list = []
for element in list_1:
    if type(element) == int:
        my_sum += element
    elif type(element) == str and ("a" in element) == 1:
        a_list.append(element)

print("Сумма всех чисел из листа =", my_sum)
print(a_list)


# Task 3
input_list = ['cat', 'dog', 'horse', 'cow']
output_tuple = tuple(input_list)
print(output_tuple)

# Task 4
family_1 = list(input('List all family 1 members with commas: ').split(","))
family_2 = list(input('List all family 2 members with commas: ').split(","))
if len(family_1) > len(family_2):
    print(family_1)
elif len(family_1) < len(family_2):
    print(family_2)
else:
    print("Equal")


# Task 5
film = {'title': 'film', 'director': 'Johny', 'year': 2000, 'budget': 210000000, 'main_actor': 'Bobby', 'slogan': 'Hi!'}
for key in film:
    print(key)
for key in film:
    print(film[key])
for item in film.items():
    print(item)


# Task 6
my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
my_sum = 0
for key in my_dictionary:
    my_sum += my_dictionary[key]
print(my_sum)


# Task 7
my_list = [1, 2, 3, 4, 5, 3, 2, 1]
my_list_2 = list(set(my_list))
print(my_list_2)


# Task 8
set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}
set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}

print("Repeated values: ", set1 & set2)
print("Unique values: ", set1 ^ set2)

if set2.issubset(set1):
    print("set2 is a subset of set1")
elif set2.issuperset(set1):
    print("set1 is a subset of set2")
else:
    print("There is no any subsets in input sets")


