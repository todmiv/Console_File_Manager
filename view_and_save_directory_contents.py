"""
Модуль view_and_save_directory_contents.py содержит функции для просмотра и сохранения содержимого директории.
"""

import os

# Функция просмотра рабочей директории
def view_directory_contents():
    """
    Выводит список всех файлов и папок в текущей рабочей директории.
    """
    contents = os.listdir()
    print("Содержимое рабочей директории:")
    for item in contents:
        print(item)


def save_directory_contents():
    """
    Сохраняет содержимое текущей директории в файл listdir.txt, разделяя файлы и папки.
    """
    contents = os.listdir()
    files = []
    dirs = []
    for item in contents:
        if os.path.isfile(item):
            files.append(item)
        else:
            dirs.append(item)
    with open("listdir.txt", "w", encoding='utf-8') as f:
        f.write("files: " + ", ".join(files) + "\n")
        f.write("dirs: " + ", ".join(dirs))
    print("Содержимое рабочей директории сохранено в файл listdir.txt")
