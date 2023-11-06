import os

# Функция просмотра рабочей директории
def view_directory_contents():
    contents = os.listdir()
    print("Содержимое рабочей директории:")
    for item in contents:
        print(item)


def save_directory_contents():
    contents = os.listdir()
    files = []
    dirs = []
    for item in contents:
        if os.path.isfile(item):
            files.append(item)
        else:
            dirs.append(item)
    with open("listdir.txt", "w") as f:
        f.write("files: " + ", ".join(files) + "\n")
        f.write("dirs: " + ", ".join(dirs))
    print("Содержимое рабочей директории сохранено в файл listdir.txt")