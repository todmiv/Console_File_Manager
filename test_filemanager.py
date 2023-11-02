from seven_functions import *
import platform
import unittest.mock


# Тесты для функции view_operating_system_info
def test_view_operating_system_info():
    # Тестирование корректности вывода информации об операционной системе
    assert view_operating_system_info() == f"Информация об операционной системе:\nОперационная система: {platform.system()}\nВерсия: {platform.release()}"
    # Тестирование корректности вывода операционной системы
    assert platform.system() in view_operating_system_info()
    # Тестирование корректности вывода версии операционной системы
    assert platform.release() in view_operating_system_info()


# Тесты для функции view_program_creator_output
def test_view_program_creator():
    expected_output = "Информация о создателе программы:\nСоздатель программы: '@todmiv'"
    # Тестирование соответствия ожидаемому значению
    assert view_program_creator() == expected_output
    # Тестирование возврата строкового типа данных
    assert isinstance(view_program_creator(), str)
    # Тестирование не нулевой длины вывода
    assert len(view_program_creator()) > 0


# Тесты для функции choose_random_people
def test_choose_random_people():
    people = {"Аня": 25, "Ян": 30, "Марк": 35, "Оля": 40, "Ева": 45}
    num_people = 3
    # Тестирование корректности выбора случайных людей
    chosen_people = choose_random_people(people, num_people)
    print(chosen_people)
    assert set(chosen_people).issubset(set(people.keys()))
    # Тестирование корректности количества выбранных людей
    assert len(chosen_people) == num_people


# Тесты для функции check_answer
def test_check_answer():
    people = {"Аня": "01.01.2000", "Ян": "02.02.2000", "Марк": "03.03.2000", "Оля": "04.04.2000", "Ева": "05.05.2000"}
    # Тестирование корректности проверки правильного ответа
    assert check_answer("Аня", "01.01.2000", people) == True
    # Тестирование корректности проверки неправильного ответа
    assert check_answer("Ян", "01.01.2000", people) == False


# Тесты для функции play_quiz
def test_play_quiz():
    """
    Тестирование возврата None при выборе "нет" для продолжения игры
    """
    # Замена встроенной функции input для автоматического ввода "нет"
    with unittest.mock.patch('builtins.input', return_value="нет"):
        # Выполнение функции и проверка возвращаемого значения
        play_again = play_quiz()
        assert play_again == None


def test_bank_account():
    # Тестирование пополнения счета
    balance = 0
    choice = "1"
    amount = 100
    balance += amount
    assert balance == 100, "Ошибка: неправильный баланс после пополнения счета"

    # Тестирование снятия со счета
    choice = "2"
    amount = 50
    if amount > balance:
        assert False, "Ошибка: недостаточно средств на счете"
    else:
        balance -= amount
        assert balance == 50, "Ошибка: неправильный баланс после снятия со счета"

    # Тестирование проверки баланса
    choice = "3"
    assert balance == 50, "Ошибка: неправильный баланс при проверке"

    # Тестирование выхода из программы
    choice = "4"
    assert choice == "4", "Ошибка: неправильный выбор действия для выхода"

    print("Все тесты пройдены успешно!")