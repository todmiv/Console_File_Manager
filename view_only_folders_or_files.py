"""
Модуль view_only_folders_or_files.py содержит функцию для просмотра только папок или только файлов.
"""

import os

# Функция просмотра только папок или файлов
def view_only_folders_or_files(choice):
    """
    Выводит список только папок (если choice == "6") или только файлов (если choice == "7") в текущей директории.

    :param choice: строка "6" для папок, "7" для файлов
    """
    contents = os.listdir()
    if choice == "6":
        print("Папки в рабочей директории:")
        for item in contents:
            if os.path.isdir(item):
                print(item)
    elif choice == "7":
        print("Файлы в рабочей директории:")
        for item in contents:
            if os.path.isfile(item):
                print(item)
