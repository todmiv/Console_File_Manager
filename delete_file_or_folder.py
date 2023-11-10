import os
from decorators import beautiful_output


# Функция удаления файла или папки
@beautiful_output
def delete_file_or_folder():
    name = input("Введите название файла или папки: ")

    action = "Файл" if os.path.isfile(name) else "Папка"

    try:
        if os.path.exists(name):
            os.remove(name) if os.path.isfile(name) else os.rmdir(name)
            result = f"{action} {name} удален{'' if os.path.isfile(name) else 'а'}."
        else:
            result = f"Файл или папка {name} не существует."
    except OSError as e:
        result = f"Ошибка при удалении {action.lower()}: {e}"

    return result
