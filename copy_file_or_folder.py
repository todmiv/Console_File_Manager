"""
Модуль copy_file_or_folder.py содержит функцию для копирования файла или папки.
"""

import os

# Функция копирования файла или папки
def copy_file_or_folder():
    """
    Запрашивает у пользователя источник и назначение, затем копирует файл или папку.
    Для папок копирует только файлы, не подпапки.
    """
    source = input("Введите название папки/файла, для копирования: ")
    destination = input("Введите новое название папки/файла: ")
    if os.path.exists(source):
        try:
            if os.path.isfile(source):
                with open(source, 'rb') as src_file:
                    with open(destination, 'wb') as dest_file:
                        dest_file.write(src_file.read())
                print(f"Файл {source} скопирован в {destination}.")
            else:
                os.makedirs(destination, exist_ok=True)
                for item in os.listdir(source):
                    item_path = os.path.join(source, item)
                    if os.path.isfile(item_path):
                        with open(item_path, 'rb') as src_file:
                            with open(os.path.join(destination, item), 'wb') as dest_file:
                                dest_file.write(src_file.read())
                print(f"Папка {source} скопирована в {destination}.")
        except Exception as e:
            print(f"Ошибка при копировании: {e}")
    else:
        print(f"Файл или папка {source} не существует.")
