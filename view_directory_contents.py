import os

# Функция просмотра рабочей директории
def view_directory_contents():
    contents = os.listdir()
    print("Содержимое рабочей директории:")
    for item in contents:
        print(item)
