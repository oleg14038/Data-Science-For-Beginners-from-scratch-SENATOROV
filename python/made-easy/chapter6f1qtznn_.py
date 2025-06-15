# %%NBQA-CELL-SEPe1e469
"""The module typing need for iteration."""
from collections.abc import Iterator


# %%NBQA-CELL-SEPe1e469
def lemonade_stall(price: int) -> None:
    """Проверяет цену.

    Выводит:. Ингредиенты напитков в зависимости от стоимости.
    """
    if price == 5:
        print("Лимонад сделан из:")
        print("Лимонный сок")
        print("Вода")
        print("Соль")
        print("Сахар")

        print("\nSprite сделан из:")
        print("Лимонный сок")
        print("Содовая")
        print("Сахар")
        print("Секретный ингредиент")
    else:
        print("Пожалуйста, заплатите нужную сумму.")


lemonade_stall(5)


# %%NBQA-CELL-SEPe1e469
def my_name(first_name: str, last_name: str) -> None:
    """Функция выводит полное имя.

    :param first_name: Имя. :param last_name: Фамилия.
    """
    print(f"Ваше имя: {first_name} {last_name}")


# Вызов функции
my_name("Oleg", "Nefedov")


# %%NBQA-CELL-SEPe1e469
def fib(max_value: int) -> None:
    """Выводит ряд Фибоначчи до числа max_value."""
    first, second = 0, 1
    while first < max_value:
        # вывод ряда Фибоначчи до max_value
        print(first, end=" ")
        first, second = second, first + second
    print()  # добавляет перевод строки в конце


# Вызовем функцию, которую мы только что определили
fib(100)


# %%NBQA-CELL-SEPe1e469
def greet(name: str, age: int) -> None:
    """Выводит приветствие с именем и возрастом.

    :param name: Имя человека. :param age: Возраст человека.
    """
    print(f"Привет, {name}. Тебе {age} лет.")


# Вызов функции с позиционными аргументами
greet("Олег", 30)


# %%NBQA-CELL-SEPe1e469
def print_numbers(*args: int) -> int:
    """Выводит заданные числа.

    :param args: Произвольное количество чисел.
    """
    for number in args:
        print(number)
    return sum(args)


# Вызов функции с передачей произвольного количества аргументов
print_numbers(1, 2, 3, 4, 5)


# %%NBQA-CELL-SEPe1e469
def print_info_data(**user_details: str) -> None:
    """Print information about the provided keyword arguments."""
    for key, value in user_details.items():
        print(f"{key}: {value}")


# Calling the function with keyword arguments
print_info_data(
    user_name="Oleg", user_age="30", user_city="Moscow"
)  # Passing keyword arguments


# %%NBQA-CELL-SEPe1e469
def full_greet(greeting: str, *args: str, **kwargs: str) -> None:
    """Print a greeting followed by positional and keyword arguments."""
    print(greeting)

    print("Positional arguments (args):")
    for arg in args:
        print(arg)

    print("Keyword arguments (kwargs):")
    for key, value in kwargs.items():
        print(f"{key}: {value}")


def print_info(**user_details: str) -> None:
    """Print information about the provided keyword arguments."""
    for key, value in user_details.items():
        print(f"{key}: {value}")


# Now, we can call the functions correctly
print_info(user_name_name="Oleg", user_full_age="30", user_city_live="Moscow")


full_greet("Hello!", "Oleg", "Ivan", age=str(30), city="Moscow")


# %%NBQA-CELL-SEPe1e469
def parrot(
    volt: int | float,
    state: str = "dead",
    act: str = "comes_to_life",
    type_color: str = "Norwegian Blue",
) -> None:
    """Функция выводит информацию о попугае в.

    зависимости от состояния и напряжения.

    :param volt: Напряжение (обязательный параметр). :param state: Состояние
    попугая (по умолчанию 'dead'). :param act: Действие попугая (по умолчанию
    'comes_to_life'). :param type_color: Тип попугая (по умолчанию 'Norwegian
    Blue')
    """
    print("- Это попугай не", act, end=" ")
    print("Even if you skip it", volt, "volt through it")
    print("-What plumage!", type_color)
    print("He", state, "!")


# 1. Позиционный аргумент
parrot(1000)

# 2. Именованный аргумент
parrot(volt=1000)

# 3. Два именованных аргумента
parrot(volt=1000000, act="It will fly")

# 4. Два именованных аргумента в другом порядке
parrot(act="It will fly", volt=1000000)

# 5. Три позиционных аргумента (обратите внимание,
# что функции паррот не хватает
# кода, чтобы обработать больше трех параметров.
# Предположим, что паррот
# ожидает до 4-х параметров)
parrot(10000, "went to the forefathers", "will jump")

# 6. Один позиционный и один именованный аргумент
parrot(100000, state="flying with angels")

# 7. Ошибка: отсутствует обязательный аргумент `volt`
# parrot()  # это вызовет ошибку TypeError,
# потому что `volt` обязательный

# 8. Ошибка: неименованный аргумент после именованного
# parrot(volt=5.0, "He died")  # Это вызовет ошибку синтаксиса.
# Нельзя передавать неименованный аргумент после именованного.

# 9. Ошибка: передача одного и того же аргумента дважды
# parrot(110, volt=220)
# # Это вызовет ошибку, потому что аргумент `volt` передается дважды

# 10. Ошибка: неизвестный именованный аргумент
# parrot(act="Jgon KLiz")  # Это вызовет ошибку,
# если `act` не является ожидаемым аргументом.
# Это не ошибка синтаксиса, но логическая ошибка,
# если аргумент `act` не предусмотрен.


# %%NBQA-CELL-SEPe1e469
def try_function(*args: str, **kwargs: str | int) -> None:
    """Функция принимает произвольное количество позиционных.

    именованных аргументов.

    :param args: Позиционные аргументы.
    которых является строкой.
    :param kwargs: Именованные аргументы, где ключи - строки.
      значения могут быть строками или числами.
    """
    print("args:", args)  # args будет кортежем строк
    print("kwargs:", kwargs)


# kwargs будет словарем, где ключи - строки, а значения - строки или числа


# Вызов функции с правильным использованием *args и **kwargs
try_function(
    "Monday",
    "Tuesday",
    "Wednesday",  # Позиционные аргументы (строки)
    fourth="Thursday",
    fifth="Friday",
    weekend1="Saturday",
    weekend2="Sunday",
    year=2024,
)  # Именованные аргументы (ключи - строки, значения - строки или числа)


# %%NBQA-CELL-SEPe1e469
def inclusive_range(*args: int) -> Iterator[int]:
    """Функция, которая генерирует последовательность.

    чисел от start до stop с шагом step.


    :param args: Позиционные аргументы.
     - 1 аргумент: stop (до этого значения, не включая).
     - 2 аргумента: start и stop.
     - 3 аргумента: start, stop, и step.
    :return: Итератор, генерирующий числа от start до stop с шагом step.
    """
    numargs = len(args)

    # начальные значения
    start = 0
    step = 1

    # проверка параметров
    if numargs < 1:
        raise TypeError(f"Expected at least one argument, got {numargs}")
    if numargs == 1:
        stop = args[0]
    if numargs == 2:
        start, stop = args
    if numargs == 3:
        start, stop, step = args
    else:
        raise TypeError(f"Expected at most 3 arguments, got {numargs}")

    # генератор
    i = start
    while i <= stop:
        yield i
        i += step
