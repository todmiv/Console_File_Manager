import os
from decorators import beautiful_output


# Функция копирования файла или папки
@beautiful_output
def copy_file_or_folder():
    source = input("Введите название папки/файла, для копирования: ")
    destination = input("Введите новое название папки/файла: ")

    if os.path.exists(source):
        is_file = os.path.isfile(source)
        action = "Файл" if is_file else "Папка"

        try:
            if is_file:
                with open(source, 'rb') as src_file, open(destination, 'wb') as dest_file:
                    dest_file.write(src_file.read())
            else:
                os.makedirs(destination)
                for item in os.listdir(source):
                    item_path = os.path.join(source, item)
                    if os.path.isfile(item_path):
                        with open(item_path, 'rb') as src_file, open(os.path.join(destination, item),
                                                                     'wb') as dest_file:
                            dest_file.write(src_file.read())

            result = f"{action} {source} скопирован{'' if is_file else 'а'} в {destination}."
        except OSError as e:
            result = f"Ошибка при копировании {action.lower()}: {e}"
    else:
        result = f"Файл или папка {source} не существует."

    return result
