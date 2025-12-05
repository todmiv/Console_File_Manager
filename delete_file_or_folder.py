"""
Модуль delete_file_or_folder.py содержит функцию для удаления файла или папки.
"""

import os

# Функция удаления файла или папки
def delete_file_or_folder():
    """
    Запрашивает у пользователя название файла или папки и удаляет его, если существует.
    Для папок удаляет только пустые.
    """
    name = input("Введите название файла или папки: ")
    if os.path.exists(name):
        try:
            if os.path.isfile(name):
                os.remove(name)
                print(f"Файл {name} удален.")
            else:
                os.rmdir(name)
                print(f"Папка {name} удалена.")
        except OSError as e:
            print(f"Ошибка при удалении {name}: {e}")
    else:
        print(f"Файл или папка {name} не существует.")
