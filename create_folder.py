import os
from decorators import beautiful_output


# Функция создание папки
@beautiful_output
def create_folder():
    folder_name = input("Введите название папки: ")

    try:
        os.mkdir(folder_name)
        result = f"Папка {folder_name} создана."
    except OSError as e:
        result = f"Ошибка при создании папки: {e}"

    return result
