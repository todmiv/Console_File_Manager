"""
Модуль create_folder.py содержит функцию для создания новой папки.
"""

import os

# Функция создание папки
def create_folder():
    """
    Запрашивает у пользователя название папки и создает ее в текущей директории.
    """
    folder_name = input("Введите название папки: ")
    try:
        os.mkdir(folder_name)
        print(f"Папка {folder_name} создана.")
    except FileExistsError:
        print(f"Папка {folder_name} уже существует.")
    except OSError as e:
        print(f"Ошибка при создании папки: {e}")
