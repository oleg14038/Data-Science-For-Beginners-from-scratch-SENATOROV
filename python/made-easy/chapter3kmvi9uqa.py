# %%NBQA-CELL-SEPe1e469
"""Chapter."""


# %%NBQA-CELL-SEPe1e469
print("Hello World ! ")


# %%NBQA-CELL-SEPe1e469
width = 20
height = 5 * 9

height
# обратите внимание, что этот код ничего не возвращает


# %%NBQA-CELL-SEPe1e469
print("C:\\some\narne")  # эдесь \n - переход на новую строку!

# C:\some
# arne


# %%NBQA-CELL-SEPe1e469
print("C:\\some\tarne")

# C:\some	arne


# %%NBQA-CELL-SEPe1e469
print(r"C:\some\name")  # r перед открывающей кавычкой

# C:\some\name


# %%NBQA-CELL-SEPe1e469
text = " Put several strings within parentheses"
text_one = "to have them joined together."

text_full = text + text_one

text_full


# %%NBQA-CELL-SEPe1e469
word = "Python"
word[0]  # символ в позиции О


# %%NBQA-CELL-SEPe1e469
word[5]  # символ в позиции 5


# %%NBQA-CELL-SEPe1e469
word[-4]


# %%NBQA-CELL-SEPe1e469
word[0:2]  # с позиции О (включительно) до 2 (не включая его)

# 'Pyth'


# %%NBQA-CELL-SEPe1e469
word[2:5]  # с позиции 2 (включительно) до 5 (не включая его)

# 'tho'


# %%NBQA-CELL-SEPe1e469
word[:2] + word[2:]

# 'Py          thon


# %%NBQA-CELL-SEPe1e469
# word[2] = "l"  # TypeError: 'str' object does not support item assignment


# %%NBQA-CELL-SEPe1e469
# встроенная функция len () возвращает длину строки
len(word)


# %%NBQA-CELL-SEPe1e469
# перенос выражения на новую строку с использованием \
expressions_firs = 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9

expressions_firs


# %%NBQA-CELL-SEPe1e469
# перенос выражения на новую строку с использованием ()
expressions_second = 1 * 2 * 3 + 7 + 8 + 9

expressions_second


# %%NBQA-CELL-SEPe1e469
# перенос выражения на новую строку с использованием []
footballer = ["МESSI", "NEYМAR", "SUAREZ"]

footballer


# %%NBQA-CELL-SEPe1e469
# перенос выражения на новую строку с использованием {}
third_expression = {1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9}

third_expression


# %%NBQA-CELL-SEPe1e469
flag = 2
ropes = 3
pole = 4

flag, ropes, pole  # (2, 3, 4)


# %%NBQA-CELL-SEPe1e469
# переменной а присваиваем значение 45
a_variabl = 45

a_variabl


# %%NBQA-CELL-SEPe1e469
a_variabl = 3 + 2

a_variabl


# %%NBQA-CELL-SEPe1e469
# 2nd_wife # нельзя

man_vs_wild = "oleg"

man_vs_wild

# "national geographic" # нельзя

data_science = "good"

data_science

sudhir22 = "434"

sudhir22

pythonl23 = "hello world"

pythonl23

# class # нельзя

# global # нельзя

tomorrow = "tomorrow "

tomorrow

Sundar_ban = "3rf"

Sundar_ban


# %%NBQA-CELL-SEPe1e469
# ряд Фибоначчи
# сумма двух элементов -- это следующий элемент ряда
# fibonacci_series

elem_fer = 0
elem_sec = 1

while elem_fer < 10:
    print(elem_fer)
    elem_fer, elem_sec = elem_sec, elem_fer + elem_sec


# %%NBQA-CELL-SEPe1e469
# тот же ряд фибоначчи

first_number, second_number = 0, 1
while first_number < 15:
    print(first_number, end=",")
    first_number, second_number = second_number, first_number + second_number

# этот код работает так же, как и первый вариант


# %%NBQA-CELL-SEPe1e469
i_one = 256 * 256
print("The value of i_one is", i_one)


# %%NBQA-CELL-SEPe1e469
# mymodule.py


def summa(*args: int) -> int:
    """
    Возвращает сумму всех переданных аргументов.

    Аргументы:.


    Возвращает:.
    int - сумма всех аргументов.
    """
    return sum(args)


# *args: int - произвольное количество целых чисел.
# Можно передать любое количество аргументов
print(summa(1, 2, 3))  # Вывод: 6
print(summa(5, 10, 15, 20))  # Вывод: 50


# %%NBQA-CELL-SEPe1e469
v_var = 5
b_one = 5
res = 5 * 6

# Используем f-строку
stroks = f"when {v_var} is multiplied by {b_one}, the result is {res}."
print(stroks)


# %%NBQA-CELL-SEPe1e469
name = "oleg"
lastname = "olegNfedov"
place = "Mirny"

print(f"{name}, {lastname} lives in {place}")


# %%NBQA-CELL-SEPe1e469
print("      /|")
print("     / |")
print("    /  |")
print("   /   |")
print("  /    |")
print(" /_____|")
