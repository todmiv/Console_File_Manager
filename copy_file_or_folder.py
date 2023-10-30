import os

# Функция копирования файла или папки
def copy_file_or_folder():
    source = input("Введите название папки/файла, для копирования: ")
    destination = input("Введите новое название папки/файла: ")
    if os.path.exists(source):
        if os.path.isfile(source):
            with open(source, 'rb') as src_file:
                with open(destination, 'wb') as dest_file:
                    dest_file.write(src_file.read())
            print(f"Файл {source} скопирован в {destination}.")
        else:
            os.makedirs(destination)
            for item in os.listdir(source):
                item_path = os.path.join(source, item)
                if os.path.isfile(item_path):
                    with open(item_path, 'rb') as src_file:
                        with open(os.path.join(destination, item), 'wb') as dest_file:
                            dest_file.write(src_file.read())
            print(f"Папка {source} скопирована в {destination}.")
    else:
        print(f"Файл или папка {source} не существует.")
