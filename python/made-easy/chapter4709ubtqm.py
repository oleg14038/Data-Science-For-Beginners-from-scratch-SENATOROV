# %%NBQA-CELL-SEPe1e469
"""Chapter4."""


# %%NBQA-CELL-SEPe1e469
import math

import numpy as np

# import random


# %%NBQA-CELL-SEPe1e469
x_num = 38

email = "olegnefedov385@gmail.com"

print(x_num)
print(email)
print(type(x_num))
print(type(email))


# %%NBQA-CELL-SEPe1e469
# import keyword

# print(keyword.kwlist)


# %%NBQA-CELL-SEPe1e469
a_nane = 5
print(id(a_nane))
print(type(a_nane))


# %%NBQA-CELL-SEPe1e469
a_num = [1, 2, 3]  # Список создаётся в памяти, а 'a' ссылается на него
b_num = a_num  # 'b' теперь содержит ссылку на тот же самый список
print(id(a_num))
print(id(b_num))
b_num[0] = 100  # Изменяем список через переменную 'b'
print(a_num)  # Вывод: [100, 2, 3] — изменения отразились и в 'a'


# %%NBQA-CELL-SEPe1e469
x_number = [1, 2, 3]
y_num = x_number
y_num.append(4)
print(x_number)  # [1, 2, 3, 4] — список изменился через ссылку 'y_num'
print(y_num)


# %%NBQA-CELL-SEPe1e469
x_numb = 10
y_number = x_numb

print(y_number)

y_number += 5  # создаётся новый объект '15'
print(x_numb)  # 10 — 'x' осталась ссылаться на прежний объект


# %%NBQA-CELL-SEPe1e469
a_b = [1, [2, 3], 4]  # Список содержит другой список
b_a = a_b[1]  # 'b' содержит ссылку на список [2, 3]

print(b_a)

# b_a[2] = 200  # Изменение вложенного списка через 'b_a'
print(a_b)  # [1, [200, 3], 4] — изменения отражаются в исходном списке


# %%NBQA-CELL-SEPe1e469
# import sys  # Импортируем модуль в начале файла

# x_gen = [1, 2, 3]
# print(sys.getrefcount(x_gen))  # Выводит количество ссылок на объект x_gen


# %%NBQA-CELL-SEPe1e469
def some_function() -> None:
    """Выполняет действие без возврата значения."""


# %%NBQA-CELL-SEPe1e469
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print(arr[..., 1])  # Вывод: [[ 2  5]
#         [ 8 11]]


# %%NBQA-CELL-SEPe1e469
def print_args(x_y: int, y_x: int, z_x: int, *args: int) -> None:
    """Выводит значения аргументов x, y, z.

    И дополнительные аргументы args.
    """
    print(f"x = {x_y}, y = {y_x}, z = {z_x}, args = {args}")


# Вызов функции с позиционными аргументами
print_args(1, 2, 3, 4, 5, 6)  # Вывод: x = 1, y = 2, z = 3, args = (4, 5, 6)


# %%NBQA-CELL-SEPe1e469
# from typing import List

# def process_data(data: List[...]) -> ...:
#     ...


# %%NBQA-CELL-SEPe1e469
my_list = [x_x if x_x % 2 == 0 else ... for x_x in range(10)]
print(my_list)  # Вывод: [0, ..., 2, ..., 4, ..., 6, ..., 8, ...]


# %%NBQA-CELL-SEPe1e469
z_one = 3 + 4j  # Здесь 3 — действительная часть, 4 — мнимая часть

RealPart = z_one.real  # Действительная часть: 3.0
ImagPart = z_one.imag  # Мнимая часть: 4.0

print(f"Действительная часть: {RealPart}, Мнимая часть: {ImagPart}")


# %%NBQA-CELL-SEPe1e469
z1 = 1 + 2j
z2 = 3 + 4j
z_sum = z1 + z2  # (1 + 3) +
# (2 + 4)j = 4 + 6j

z_diff = z1 - z2  # (1 - 3) +
# (2 - 4)j = -2 - 2j

z_product = z1 * z2  # (1 * 3 - 2 * 4) +
# (1 * 4 + 2 * 3)j = -5 + 10j

z_quotient = z1 / z2  # ((1 * 3 + 2 * 4) /
# (3^2 + 4^2)) + ((2 * 3 - 1 * 4) / (3^2 + 4^2))j


print(f"{z_sum}\n{z_diff}\n{z_product}\n{z_quotient}")


# %%NBQA-CELL-SEPe1e469
b_s = "nilabh"  # строка, символ ' n ' находится на 0-м индексе,
# а ' h ' - на 5-м

print(b_s[3])  # срез строки по индексу 3 дает "а"


# %%NBQA-CELL-SEPe1e469
# Получаем код для символа 'A'
code_a = ord("A")
print(code_a)  # Вывод: 65

# Получаем код для символа 'a'
code_a_lower = ord("a")
print(code_a_lower)  # Вывод: 97

# Получаем код для символа '1'
code_one = ord("1")
print(code_one)  # Вывод: 49

# Получаем код для символа '!'
code_exclamation = ord("!")
print(code_exclamation)  # Вывод: 33


# %%NBQA-CELL-SEPe1e469
# Получаем символ для кодовой точки 65
char_a = chr(65)
print(char_a)  # Вывод: 'A'

# Получаем символ для кодовой точки 97
char_a_lower = chr(97)
print(char_a_lower)  # Вывод: 'a'

# Получаем символ для кодовой точки 49
char_one = chr(49)
print(char_one)  # Вывод: '1'

# Получаем символ для кодовой точки 33
char_exclamation = chr(33)
print(char_exclamation)  # Вывод: '!'


# %%NBQA-CELL-SEPe1e469
# Создание байтовой строки с помощью литерала
byte_str = b"Hello, World!"
print(byte_str)  # Вывод: b'Hello, World!'


# %%NBQA-CELL-SEPe1e469
# Создание байтовой строки с помощью функции bytes()
byte_str_from_list = bytes([72, 101, 108, 108, 111])
# ASCII-коды для 'Hello'

print(byte_str_from_list)  # Вывод: b'Hello'


# %%NBQA-CELL-SEPe1e469
# Создание байтового массива с начальным содержимым
byte_array_with_data = bytearray([65, 66, 67])

# ASCII-коды для 'A', 'B', 'C'
print(byte_array_with_data)  # Вывод: bytearray(b'ABC')


# %%NBQA-CELL-SEPe1e469
# def find_maximum(number_1: int, number_2: int) -> int:
#     """Return the larger of two number.

#     The function compares two integers and returns the larger one.
#     """
#     number_1 = random.randint(1, 5)
#     number_2 = random.randint(1, 5)
#     if number_1 > number_2:
#         result: int = number_1
#         print("The number_1 variable is reassigned to the result variable")

#     else:
#         print("The number_2 variable is reassigned to the result variable")

#     return result


# %%NBQA-CELL-SEPe1e469
text_str = "hello, world"
print(text_str.upper())  # Выведет: HELLO, WORLD


# %%NBQA-CELL-SEPe1e469
text_one = "hello, world"
new_text = text_one.replace("world", "Python")
print(new_text)  # Выведет: hello, Python


# %%NBQA-CELL-SEPe1e469
# Пример 3: Метод .strip()

# Удаляет пробелы в начале и конце строки.


text_two = "   hello, world   "
print(text_two.strip())  # Выведет: hello, world


# %%NBQA-CELL-SEPe1e469
# Пример 4: Метод .append()

# Добавляет элемент в конец списка.

numb = [1, 2, 3]
numb.append(4)
print(numb)  # Выведет: [1, 2, 3, 4]


# %%NBQA-CELL-SEPe1e469
# Пример 5: Метод .remove()

# Удаляет первое вхождение элемента из списка

fruits = ["apple", "banana", "cherry", "apple"]
fruits.remove("apple")
print(fruits)  # Выведет: ['banana', 'cherry', 'apple']


# %%NBQA-CELL-SEPe1e469
# Пример 6: Метод .sort()

# Сортирует список по возрастанию.

number = [4, 1, 3, 2]
number.sort()
print(number)  # Выведет: [1, 2, 3, 4]


# %%NBQA-CELL-SEPe1e469
person = {"name": "Alice", "age": 25, "city": "New York"}
print(person.keys())  # Выведет: dict_keys(['name', 'age', 'city'])

# Пример 8: Метод .values()
# Возвращает список всех значений словаря
print(person.values())  # Выведет: dict_values
# (['Alice', 25, 'New York'])

# Пример 9: Метод .items()
# Возвращает список пар "ключ-значение" в виде кортежей.

print(person.items())  # Выведет: dict_items([('name', 'Alice'),
# ('age', 25), ('city', 'New York')])


# %%NBQA-CELL-SEPe1e469
# Пример 10: Метод .add()
# Добавляет элемент в множество.

numbers = {1, 2, 3}
numbers.add(4)
print(numbers)  # Выведет: {1, 2, 3, 4}

# Удаляет элемент из множества.
numbers.remove(2)
print(numbers)  # Выведет: {1, 3, 4}


# %%NBQA-CELL-SEPe1e469
# Пример 12: Метод .union()

# Возвращает объединение двух множеств.

set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
print(union_set)  # Выведет: {1, 2, 3, 4, 5}


# %%NBQA-CELL-SEPe1e469
# Пример 13: Метод .read()

# Чтение содержимого файла.

# with open('example.txt', 'r') as file:
#     content = file.read()
#     print(content)


# %%NBQA-CELL-SEPe1e469
# Пример 14: Метод .write()

# Запись данных в файл.

# with open('example.txt', 'w') as file:
#     file.write("Hello, world!")


# %%NBQA-CELL-SEPe1e469
# Пример 15: Метод .close()

# Закрытие файла (автоматически вызывается при использовании with)

# file = open('example.txt', 'r')
# file.close()


# %%NBQA-CELL-SEPe1e469
# 1. len()

# Возвращает длину (количество элементов) объекта (например,
#  строки, списка, кортежа, словаря).

# Пример с строкой
text = "Hello"
print(len(text))  # Выведет: 5

# Пример со списком
num = [1, 2, 3, 4, 5]
print(len(num))  # Выведет: 5


# %%NBQA-CELL-SEPe1e469
# 2. abs()

# Возвращает абсолютное значение числа.

value = -10
print(abs(value))  # Выведет: 10


# %%NBQA-CELL-SEPe1e469
# 3. sum()

# Возвращает сумму элементов итерируемого
# объекта (например, список или кортеж).

coun = [1, 2, 3, 4, 5]
print(sum(coun))  # Выведет: 15


# 4. min() и max()

# Возвращают минимальное и максимальное значение
# из последовательности или набора чисел

print(min(coun))  # Выведет: 1
print(max(coun))  # Выведет: 9


# %%NBQA-CELL-SEPe1e469
# 4. min() и max()

# Возвращают минимальное и максимальное
# значение из последовательности или набора чисел.


# %%NBQA-CELL-SEPe1e469
# 5. round()

# Округляет число до заданного количества
# знаков после запятой (по умолчанию до ближайшего целого).

constant_value = 3.14159
print(round(constant_value, 2))  # Выведет: 3.14

# Округление до ближайшего целого
# print(round(5.6))  # Выведет: 6


# %%NBQA-CELL-SEPe1e469
# 6. type()

# Возвращает тип объекта.

obj = 42
print(type(obj))  # Выведет: <class 'int'>

text_three = "Hello"
print(type(text_three))  # Выведет: <class 'str'>

# 7. isinstance()

# Проверяет, принадлежит ли объект
# к определённому типу данных

print(isinstance(obj, int))  # Выведет: True
print(isinstance(text_three, str))  # Выведет: True


# %%NBQA-CELL-SEPe1e469
# 8. enumerate()

# Возвращает объект, который генерирует кортежи,
# содержащие индекс и соответствующий элемент последовательности.

fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# Выведет:
# 0: apple
# 1: banana
# 2: cherry


# %%NBQA-CELL-SEPe1e469
# 9. zip()

# Объединяет несколько итерируемых объектов (например, списки)
# в кортежи, где первый элемент каждого кортежа будет взят
# из соответствующего итерируемого объекта.

names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 95]

for name, score in zip(names, scores):
    print(f"{names}: {score}")

# Выведет:
# Alice: 85
# Bob: 90
# Charlie: 95


# %%NBQA-CELL-SEPe1e469
# 10. sorted()

# Возвращает отсортированную версию итерируемого объекта
# (например, список), не изменяя оригинал.

numbers_val = [5, 2, 9, 1, 5, 6]
sorted_numbers = sorted(numbers_val)
print(sorted_numbers)  # Выведет: [1, 2, 5, 5, 6, 9]

# Оригинальный список не изменён
print(numbers_val)  # Выведет: [5, 2, 9, 1, 5, 6]


# %%NBQA-CELL-SEPe1e469
# # Пример с all()
# print(all([True, True, False]))  # Выведет: False

# # Пример с any()
# print(any([False, False, True]))  # Выведет: True


# %%NBQA-CELL-SEPe1e469
# 13. filter()

# Фильтрует элементы итерируемого объекта на основе функции,
# которая возвращает True или False.

numbers_one = [1, 2, 3, 4, 5, 6]

# Оставляем только чётные числа
even_numbers = filter(lambda x: x % 2 == 0, numbers_one)
print(list(even_numbers))  # Выведет: [2, 4, 6]


# %%NBQA-CELL-SEPe1e469
# # 15. eval()

# # Выполняет строковое выражение как Python-код.
# # Будьте осторожны при использовании eval(),
# # так как оно может быть небезопасным

# expression = "2 + 3 * 5"
# result_3 = eval(expression)
# print(result_3)  # Выведет: 17


# %%NBQA-CELL-SEPe1e469
# # 16. open()

# # Открывает файл для чтения или записи.

# # Открываем файл для записи
# with open('example.txt', 'w') as file:
#     file.write("Hello, World!")

# # Открываем файл для чтения
# with open('example.txt', 'r') as file:
#     content = file.read()
#     print(content)  # Выведет: Hello, World!


# %%NBQA-CELL-SEPe1e469
# 1. Простой класс
# Пример 1: Класс Dog


class Dog:
    """Класс для представления собак."""

    def __init__(self, name_dog: str, age_dog: int):
        """Инициализация атрибутов собаки."""
        self.name_dog: str = name_dog
        self.age_dog: int = age_dog

    def bark(self) -> str:
        """Издает лай."""
        return f"{self.name_dog} говорит: Гав!"


# Создание экземпляра класса
my_dog = Dog("Бобик", 3)

# Вызов метода
print(my_dog.bark())  # Выведет: Бобик говорит: Гав!


# %%NBQA-CELL-SEPe1e469
# Пример 2: Класс Circle


class Circle:
    """Класс для представления круга."""

    def __init__(self, radius: float):
        """Инициализация радиуса круга."""
        self.radius = radius

    def area(self) -> float:
        """Возвращает площадь круга."""
        return math.pi * (self.radius**2)

    def circumference(self) -> float:
        """Возвращает длину окружности."""
        return 2 * math.pi * self.radius


# Создание экземпляра класса
circle = Circle(10)

# Вызов методов
print(f"Площадь круга: {circle.area():.2f}")  # Выведет: Площадь круга: 78.54
print(
    f"Длина окружности: {circle.circumference():.2f}"
)  # Выведет: Длина окружности: 31.42


# %%NBQA-CELL-SEPe1e469
# 14 + 26 # целочисленное сложение


# %%NBQA-CELL-SEPe1e469
# 1.5 * 4 # умножение вещественных чисел


# %%NBQA-CELL-SEPe1e469
# 2**100 # 2 в степени 100


# %%NBQA-CELL-SEPe1e469
# 4/2 # деление всегда возвращает число с плавающей точкой


# %%NBQA-CELL-SEPe1e469
# 5 > 4 # логическое выражение


# %%NBQA-CELL-SEPe1e469
z_num = [1, 2, 3]
b_number = z_num  # b ссылается на тот же объект, что и a

print(
    z_num is b_number
)  # True, так как обе переменные ссылаются на один и тот же объект


# %%NBQA-CELL-SEPe1e469
# Строка
word = "hello"

print("h" in word)  # True, так как "h" есть в строке


# %%NBQA-CELL-SEPe1e469
Length = 5
Width = 8
Area = Length * Width
print("Area of the Rectangle is", Area)
print(" Perimeter of the rectangle is", 2 * (Length + Width))


# %%NBQA-CELL-SEPe1e469
# эдесь две физические и две логические строки
i_number = 5
print(i_number)


# %%NBQA-CELL-SEPe1e469
# эдесь одна физическая строка, но две логические
i_one = 5
print(i_one)
