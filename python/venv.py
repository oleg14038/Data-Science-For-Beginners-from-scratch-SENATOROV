"""Issue venv."""

from PIL import Image

#     1. python -m venv venv - создаёт виртуальное окружение в папке venv.
#
#     Разбор:
#
#     python -m venv — запускает модуль venv, встроенный в Python.
#
#     venv (второй аргумент) — имя папки, в которой будет
#     создано виртуальное окружение
#
#
#     Создаётся каталог venv.
#     Внутри него создаются подпапки (bin, lib, include и др.).
#     Копируется исполняемый файл Python.
#     Устанавливается локальный менеджер пакетов pip.
#
#     После создания окружения его нужно активировать
#     перед установкой
#     зависимостей: venv\Scripts\activate,
#
#     Windows (PowerShell): venv\Scripts\Activate.ps1
#
#     Linux/macOS: source venv/bin/activate
#
#
#

#     1.1  pip list - выводит список установленных пакетов в текущем окружении Python.
#
#     Package    Version
#     ---------- -------
#     pip        23.0.1
#     setuptools 65.5.0
#     wheel      0.38.4
#     numpy      1.24.2
#     pandas     1.5.3
#
#
#     Полезные флаги:
#
#     pip list --format=columns — (по умолчанию) вывод в виде таблицы.
#
#     pip list --format=freeze — формат, совместимый с requirements.txt.
#
#     pip list --outdated — показывает устаревшие пакеты.
#
#     pip list --not-required — пакеты, не являющиеся зависимостями других.
#
#     Сохранение списка пакетов в файл
#
#
#         1. pip freeze > requirements.txt - Создаст файл requirements.txt, который можно использовать для установки зависимостей в другом окружении
#
#         2. pip install -r requirements.txt - Устанавливает пакеты, указанные в requirements.txt.
#
#
#
#
#

# 2. Что делает каждая команда в списке ниже ?
#
#     1. conda env list or conda info --envs - выводит список всех существующих виртуальных окружений Conda.
#
#
#     Пример вывода:
#
#     conda environments:
#     base                  *  /home/user/miniconda3
#
#     ml_env                  /home/user/miniconda3/envs/ml_env
#
#     data_env                /home/user/miniconda3/envs/data_env
#
#
#     base — базовое окружение Conda, создаётся при установке.
#
#     * — текущее активное окружение.
#
#     Остальные строки — пользовательские окружения и их пути.
#
#
#
#
#
#     2. conda create -n env_name python=3.5 - cоздаёт новое виртуальное
#     окружение Conda с именем env_name и устанавливает в него Python 3.5.
#
#
#
#     3. conda env update -n env_name -f file.yml — Обновляет существующее окружение env_name на основе конфигурации из файла file.yml.
#
#
#     4. После создания: conda activate env_name
#     5. Деактивировать: conda deactivate
#
#
#
#
#     6. conda clean — очищает различные кеши и временные файлы.
#
#     -a — опция, которая указывает на полную очистку,
#     включая все пакеты и кеши.
#
#
#

imag = Image.open("C:/Users/adm/Pictures/VENV1.PNG")
imag

3.0
imag1 = Image.open("C:/Users/adm/Pictures/VENV2.PNG")
imag1

imag2 = Image.open("C:/Users/adm/Pictures/VENV3.PNG")
imag2

# 4 Как установить необходимые пакеты внутрь виртуального окружения для conda/venv?
#
#         1. Установите нужные пакеты через pip: pip install numpy pandas scikit-learn
#
#         Чтобы сохранить установленные пакеты в файл, используйте: pip freeze > requirements.txt
#
#         Для установки из файла: pip install -r requirements.txt
#
#         2. В conda (анаконда/минниконда)
#
#         Установка пакетов: conda install numpy pandas scikit-learn
#
#         Если нужен пакет из pip, можно выполнить: pip install some-package
#
#         Чтобы сохранить список установленных пакетов: conda list --explicit > environment.txt
#
#         Для восстановления окружения: conda create --name SENATOROV --file environment.txt
#
#
#
#
#
#
#
#
#

# 5. pip freeze > requirements.txt
#
#     conda env export > environment.yml - Эти команды используются для сохранения списка установленных пакетов, чтобы в будущем можно было легко восстановить окружение.
#
#
#

# +
5.1
imag3 = Image.open("C:/Users/adm/Pictures/VENV4.PNG")

imag3
# -

# 6. pip install -r requirements.txt (для venv) - Устанавливает библиотеки, перечисленные в requirements.txt, с указанными версиями.
#
#     Как использовать?
#
#     Активируйте виртуальное окружение (venv):
#
#     source VENV/bin/activate  # (Linux/macOS)
#
#     VENV\Scripts\activate      # (Windows)
#
#     Установите зависимости: pip install -r requirements.txt
#
#
#
#     conda env create -f environment.yml (для conda) - Создаёт новое окружение и устанавливает пакеты из environment.yml.
#
#     Как использовать?
#
#     conda env create -f environment.yml
#     conda activate SENATOROV
#

# 7. pip list -  Выводит список всех установленных пакетов в текущем виртуальном окружении.
#
#     pip show <package> -  Отображает подробную информацию о конкретном пакете.
#
#     conda list -  Выводит список установленных пакетов в текущем conda-окружении.

# 8. По умолчанию больше пакетов устанавливается в conda, потому что:
#
#     conda включает базовое окружение, в котором уже есть библиотеки (например, numpy, pandas, scipy, matplotlib).
#
#     venv создаёт пустое окружение, в котором только pip и базовые инструменты Python.

# +
9.0
imag4 = Image.open("C:/Users/adm/Pictures/VENV5.PNG")

imag4
# -

# 10. Зачем нужно виртуальное окружение (venv, conda)?
#
#         Виртуальное окружение создаёт изолированную среду для работы с Python-проектом, чтобы избежать конфликтов версий библиотек и зависимостей.
#
#         Конфликты версий пакетов
#
#             Один проект требует numpy==1.21.0, а другой numpy==1.23.5.
#
#             Если установить новую версию numpy, старый проект может перестать работать.
#
#         Загрязнение глобального окружения
#
#             Все библиотеки устанавливаются в системный Python.
#
#             При обновлении одной библиотеки могут сломаться другие проекты.
#
#         Сложности с разными версиями Python
#
#             Один проект требует Python 3.8, другой Python 3.10.
#
#             Без виртуального окружения приходится менять глобальную версию Python.
#
#         Как помогает виртуальное окружение?
#
#         ✅ Изоляция
#
#             Каждый проект имеет свои библиотеки и свою версию Python.
#
#             Библиотеки устанавливаются в папку окружения (venv/ или conda env).
#
#         ✅ Разные версии пакетов для разных проектов
#
#             В одном окружении можно установить Django 3.2, а в другом Django 4.1, и они не конфликтуют.
#
#         ✅ Легче делиться проектом
#
#             Вместо установки всех библиотек вручную, можно передать файл requirements.txt или environment.yml, и коллега сможет развернуть окружение одной командой.
#
#         ✅ Работа без прав администратора
#
#             Все пакеты устанавливаются в папку окружения, а не в систему.
#
#             Можно работать в venv или conda без доступа к глобальному Python.
#
#         Как создать и использовать виртуальное окружение?
#         venv (стандартный инструмент Python)
#
#         python -m venv myenv  # Создание окружения
#
#         source myenv/bin/activate  # (Linux/macOS)
#
#         myenv\Scripts\activate  # (Windows)
#
# pip install -r requirements.txt  # Установка зависимостей
#
#
# conda (используется в Data Science)
#
# conda create --name myenv python=3.9  # Создание окружения
#
# conda activate myenv  # Активация
#
# conda install numpy pandas  # Установка библиотек
#
#
