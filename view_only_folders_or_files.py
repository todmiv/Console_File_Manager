import os
from decorators import beautiful_output


# Функция просмотра только папок или файлов
@beautiful_output
def view_only_folders_or_files(choice):
    contents = os.listdir()
    result = []

    if choice == "6":
        result.append("Папки в рабочей директории:")
        result.extend([item for item in contents if os.path.isdir(item)])
    elif choice == "7":
        result.append("Файлы в рабочей директории:")
        result.extend([item for item in contents if os.path.isfile(item)])

    return result
