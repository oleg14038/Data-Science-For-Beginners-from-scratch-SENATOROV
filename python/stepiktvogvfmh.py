# %%NBQA-CELL-SEPe1e469
"""Модуль для демонстрации работы с уровнями сотрудников и их категориями."""


# %%NBQA-CELL-SEPe1e469
workers = [
    ["Ivan", "Ivanov", 100000, 2],
    ["Petr", "Petrov", 150000, 2],
    ["Sidor", "Sidorov", 200000, 3],
]

# Перебор списка workers для вывода и анализа уровня сотрудников
for worker in workers:
    name, surname, salary, level = worker
    print(f"Level of {name} {surname}: {level}")

    # Приведение уровня к целому числу
    level = str(level)
    # Обработка уровня сотрудника
    if str(level) > "2":
        print("junior")
    elif str(level) >= "2":
        print("middle")
    else:
        print("senior")
