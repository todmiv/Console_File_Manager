import os

# Функция создание папки
def create_folder():
    folder_name = input("Введите название папки: ")
    os.mkdir(folder_name)
    print(f"Папка {folder_name} создана.")