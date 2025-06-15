# %%NBQA-CELL-SEPe1e469
"""from typing import List: для работы с типами списков."""

from typing import List


# %%NBQA-CELL-SEPe1e469
x_one = 4
if x_one > 0:
    if x_one % 2 == 0:
        print("x_one положительное четное число")
    else:
        print("x_one положительное нечетное число")
else:
    print("x_one отрицательное число")


# %%NBQA-CELL-SEPe1e469
x_two = 8

# Упрощенное сравнение
if 5 < x_two < 10:
    print("x_two находится между 5 и 10")
    # Оба условия проверяются одновременно

if x_two < 3 or x_two > 7:
    print(
        "x_two меньше 3 или больше 7"
    )  # Достаточно, чтобы одно из условий было истинным


# %%NBQA-CELL-SEPe1e469
nurn = int(input("Enter a number: "))
if nurn > 11:
    print(f"{nurn} i s greater than ")
else:
    print(f"{nurn} is smaller than 11")


# %%NBQA-CELL-SEPe1e469
x_entr = int(input("Please enter an integer :"))
if x_entr < 0:
    print("Negative NumЬer")
elif x_entr == 0:
    print("Zero")
elif x_entr == 1:
    print("Single")
else:
    print("More")


# %%NBQA-CELL-SEPe1e469
words = ["cat", "window"]
for w_i in words:
    print(w_i, len(w_i))


# %%NBQA-CELL-SEPe1e469
numbers = [1, 2, 3, 4]
for iteration in numbers:
    print(iteration)

print("This is end the code")


# %%NBQA-CELL-SEPe1e469
# Объявляем список для хранения чисел
integer_list: List[int] = []

# Используем другую переменную для цикла
for value_one in range(5):
    integer_list.append(value_one)
    # Добавляем текущее число в список

print(integer_list)  # Выводим список чисел


# %%NBQA-CELL-SEPe1e469
checklist = ["Mary", "had", "little", "lamb"]
for index, item in enumerate(checklist):
    print(index, item)


# %%NBQA-CELL-SEPe1e469
print(list(range(10)))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


# %%NBQA-CELL-SEPe1e469
max_value = 10  # Максимальное значение для суммирования
summa = 0  # Переменная для хранения суммы
val_two = 1  # Начальное значение для суммирования

while val_two <= max_value:
    summa += val_two  # Суммируем текущее значение
    val_two += 1  # Увеличиваем значение на 1

print(f"The sum is {summa}")  # Выводим сумму


# %%NBQA-CELL-SEPe1e469
numbers_one = [1, 2, 3, 4]

for inter in numbers_one:
    print(inter)
    break
else:
    print("this is end of the code")
print("This line outside the loop")


# %%NBQA-CELL-SEPe1e469
for number_two in range(2, 10):
    # Цикл для проверки чисел от 2 до 9
    for divisor in range(2, number_two):
        # Проверяем делители от 2 до текущего числа
        if number_two % divisor == 0:
            # Если число делится на делитель без остатка
            print(
                number_two, "equals", divisor, "*", number_two // divisor
            )  # Число не простое
            break  # Прерываем цикл, так как число не простое
    else:
        # Цикл завершён без нахождения делителя, число простое
        print(number_two, "is a prime number")


# %%NBQA-CELL-SEPe1e469
for alphabet in "python":
    if alphabet == "t":
        continue  # Пропустить итерацию, если символ "t"
    print(alphabet)

print("The end")  # Финальный вывод после завершения цикла


# %%NBQA-CELL-SEPe1e469
for num_val in range(2, 10):
    if num_val % 2 == 0:  # четное число
        print("Found an even number", num_val)
        continue
    print("Found a number", num_val)


# %%NBQA-CELL-SEPe1e469
item_value = 105
if item_value >= 100:
    print(f"Value of item_value is {item_value}")


# %%NBQA-CELL-SEPe1e469
current_number = 12
if current_number == 10:
    print("current_number is equal to 10")


# %%NBQA-CELL-SEPe1e469
value_a = 90
value_b = 103

if value_a <= 100:
    print("Value of value_a is less than 100")
if value_b <= 100:
    print("Value of value_b is less than 100")


# %%NBQA-CELL-SEPe1e469
# Запрос цены покупки и продажи у трейдера
purchase_price = float(input("Введите цену покупки: "))
selling_price = float(input("Введите цену продажи: "))

# Расчет прибыли или убытка
profit_loss = selling_price - purchase_price

# Проверка, есть ли прибыль или убыток
if profit_loss > 0:
    print(f"Трейдер получил прибыль в размере {profit_loss:.2f} единиц.")
elif profit_loss < 0:
    print(f"Трейдер понес убыток в размере {abs(profit_loss):.2f} единиц.")
else:
    print("Трейдер не получил ни прибыли, ни убытка.")


# %%NBQA-CELL-SEPe1e469
value_f = 123.456789

print(f"Значение: {value_f:.5f}")  # Вывод: Значение: 123.46


# %%NBQA-CELL-SEPe1e469
complex_number = 3 + 4j
print(abs(complex_number))

# Вывод: 5.0 (это длина вектора в комплексной плоскости)


# %%NBQA-CELL-SEPe1e469
def is_leap(year: int) -> bool:
    """Проверяет, является ли год високосным."""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


try:
    # Запрашиваем год у пользователя
    year_input = int(input("Введите год: "))

    # Проверяем, является ли год високосным
    if is_leap(year_input):
        print(f"Год {year_input} является високосным.")
    else:
        print(f"Год {year_input} не является високосным.")
except ValueError:
    print("Пожалуйста, введите корректное целое число.")
