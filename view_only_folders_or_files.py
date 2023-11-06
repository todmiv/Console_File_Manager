import os

# Функция просмотра только папок или файлов
def view_only_folders_or_files(choice):
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
