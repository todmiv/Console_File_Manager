import os
from decorators import beautiful_output


# Функция просмотра рабочей директории
@beautiful_output
def view_directory_contents():
    contents = os.listdir()
    result = ["Содержимое рабочей директории:"]
    result.extend([item for item in contents])

    return result


@beautiful_output
def save_directory_contents():
    contents = os.listdir()
    files = [item for item in contents if os.path.isfile(item)]
    dirs = [item for item in contents if os.path.isdir(item)]

    try:
        with open("listdir.txt", "w") as f:
            f.write("files: " + ", ".join(files) + "\n")
            f.write("dirs: " + ", ".join(dirs))

        result = "Содержимое рабочей директории сохранено в файл listdir.txt"
    except OSError as e:
        result = f"Ошибка при сохранении содержимого рабочей директории: {e}"

    return result
