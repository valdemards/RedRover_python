from functools import reduce
from datetime import datetime
import my_calc
from my_calc import multiply
import sys
from pprint import pprint
# pprint(sys.path)

import time
# # 4.1. Напишите функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения (с помощью кортежа):
# #      периметр квадрата, площадь квадрата и диагональ квадрата.
# def square(a):
#     return (4 * a, a * a, round(2 ** 0.5 * a, 3))
#
#
# print(square(2))
#
#
# # 4.2. Напишите фукнцию, которая принимает произвольное количество именнованных аргументов и выводит их построчно
# #      в формате аргумент: значение. Например:
# # 	name: John
# # 	last_name: Smith
# # 	age: 35
# # 	position: web developer
# def dict_printer(dict):
#     for key, value in dict.items():
#         print(key, ':', value)
#
# dict = {'name': 'John',
#         'last_name': 'Smith',
#         'age': 35,
#         'position': 'web developer'}
#
# dict_printer(dict)


# # 4.3. Используя лямбда-выражение, из списка my_list = [20, -3, 15, 2, -1, -21] создайте новый список, содержащий только
#      положительные числа
# list4_3 = list(filter(lambda x: x > 0, [20, -3, 15, 2, -1, -21]))
# print(list4_3)
#
#
# # 4.4. Используя лямбда выражение, получите результат перемножения значений в предыдущем списке
# list4_4 = reduce(lambda x, y: x * y, list4_3)
# print(list4_4)
#
#
# # 4.5. Напишите декоратор, который высчитывает время работы функции, которую он принимает в качестве параметра
# def decorator_function(func):
#     def wrapper(*args):
#         start_time = datetime.now()
#         func(*args)
#         end_time = datetime.now()
#         duration = (end_time - start_time).total_seconds()
#         return f'Duration of {func.__name__} execution was: {duration} seconds'
#     return wrapper
#
# @decorator_function
# def square(a):
#     time.sleep(1)
#     print(a**100)
#
# print(square(5))

#
# # 4.6. Создайте файл my_calc.py и пропишите в нем минимум 4 функции, выполняющие базовые арифметические вычисления.
# #      Примените эти функции в качестве методов в другом файле.
print(multiply(2, 3))
print(my_calc.divide(9, 3))
print(my_calc.plus(7, 5))
print(my_calc.minus(9, 3))
