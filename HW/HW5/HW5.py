# 5.1. Создайте любой класс с произвольным количеством подклассов, экземпляров, атрибутов и методов
#    - как минимум один атрибут должен быть с уровнем доступа private. Соответственно, для получения значений этого атрибута  нужно использовать методы get и set
# 5.2. Создайте репозиторий на Github и отправьте файл с домашним заданием в этот удаленный репозиторий
class Person:

        def __init__(self, name, surname, age):
            self.name = name
            self.surname = surname
            self.age = age


        def hello(self):
            print(f'Hello {self.name} {self.surname} !')


person_1 = Person('Bob', 'Ivanov', 23)
person_1.hello()
print()

class Employee(Person):
    def __init__(self, name, surname, age, __position, __salary):
        super().__init__(name, surname, age)
        self._position = __position
        self.__salary = __salary


    def print_salary(self):
        print(self.__salary)

emp_1 = Employee('Bob', 'Ivanov', 23, 'qa', 5000)
emp_1.hello()
print(emp_1._position)
emp_1.print_salary()