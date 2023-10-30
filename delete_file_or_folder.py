import os

# Функция удаления файла или папки
def delete_file_or_folder():
    name = input("Введите название файла или папки: ")
    if os.path.exists(name):
        if os.path.isfile(name):
            os.remove(name)
            print(f"Файл {name} удален.")
        else:
            os.rmdir(name)
            print(f"Папка {name} удалена.")
    else:
        print(f"Файл или папка {name} не существует.")
