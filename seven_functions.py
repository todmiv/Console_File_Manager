import os
import platform
import random


# Функция просмотра информации об операционной системе
def view_operating_system_info():
    output = "Информация об операционной системе:\n"
    output += f"Операционная система: {platform.system()}\n"
    output += f"Версия: {platform.release()}"
    return output


# Функция просмотр информации о создателе программы
def view_program_creator():
    output = "Информация о создателе программы:\n"
    output += "Создатель программы: '@todmiv'"
    return output


# Функции игры викторина
def choose_random_people(people, num_people):
    return random.sample(list(people.keys()), num_people)

def check_answer(person, date, people):
    if date == people[person]:
        return True
    else:
        return False

def play_quiz():
    people = {
        "Пушкин Александр Сергеевич": "26.05.1799",
        "Толстой Лев Николаевич": "09.09.1828",
        "Достоевский Федор Михайлович": "11.11.1821",
        "Чехов Антон Павлович": "29.01.1860",
        "Тургенев Иван Сергеевич": "28.10.1818",
        "Гоголь Николай Васильевич": "01.04.1809",
        "Лермонтов Михаил Юрьевич": "15.10.1814",
        "Пастернак Борис Леонидович": "10.02.1890",
        "Ахматова Анна Андреевна": "23.06.1889",
        "Маяковский Владимир Владимирович": "19.07.1893"
    }

    while True:
        random_people = choose_random_people(people, 5)

        correct_answers = 0
        wrong_answers = 0

        for person in random_people:
            date = input(f"Введите дату рождения для {person}: ")

            if check_answer(person, date, people):
                print("Правильно!")
                correct_answers += 1
            else:
                print(f"Неправильно. Правильный ответ: {person} родился {people[person]}")
                wrong_answers += 1

        print(f"Правильных ответов: {correct_answers}")
        print(f"Неправильных ответов: {wrong_answers}")

        play_again = input("Хотите начать снова? (да/нет): ")
        if play_again.lower() != "да":
            break


# Функция работы с банковским счетом
def bank_account():
    balance = 0  # начальный баланс счета
    while True:
        print("Выберите действие:")
        print("1 - Пополнить счет")
        print("2 - Снять со счета")
        print("3 - Проверить баланс")
        print("4 - Выйти из программы")
        choice = input("Введите номер действия: ")
        if choice == "1":
            amount = float(input("Введите сумму для пополнения: "))
            balance += amount
            print(f"Счет пополнен на {amount} рублей. Текущий баланс: {balance} рублей.")
        elif choice == "2":
            amount = float(input("Введите сумму для снятия: "))
            if amount > balance:
                print("На счете недостаточно средств.")
            else:
                balance -= amount
                print(f"Со счета снято {amount} рублей. Текущий баланс: {balance} рублей.")
        elif choice == "3":
            print(f"Текущий баланс: {balance} рублей.")
        elif choice == "4":
            print("Работа с банковским счетом завершена.")
            break
        else:
            print("Некорректный ввод. Попробуйте еще раз.")


# Функция изменения рабочей директории
def change_working_directory():
    path = input("Введите путь к новой рабочей директории: ")
    if os.path.exists(path):
        os.chdir(path)
        print(f"Рабочая директория изменена на {path}.")
    else:
        print(f"Путь {path} не существует.")
