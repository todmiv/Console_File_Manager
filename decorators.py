# Функция - декоратор более красивого вывода
def beautiful_output(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print("Результат:")
        print("------------------------")
        print(result)
        print("------------------------")
    return wrapper
