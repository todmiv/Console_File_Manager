from create_folder import create_folder as cf
from delete_file_or_folder import delete_file_or_folder as dfof
from copy_file_or_folder import copy_file_or_folder as cfof
from view_directory_contents import view_directory_contents as vdc
from view_only_folders_or_files import view_only_folders_or_files as vofof
from five_functions import *

def exit_program():
    print("Выход из программы.")
    exit()


def main():
    while True:
        print("Меню:")
        print("1. Создать папку")
        print("2. Удалить (файл/папку)")
        print("3. Копировать (файл/папку)")
        print("4. Просмотр содержимого рабочей директории")
        print("5. Посмотреть только папки")
        print("6. Посмотреть только файлы")
        print("7. Просмотр информации об операционной системе")
        print("8. Создатель программы")
        print("9. Играть в викторину")
        print("10. Мой банковский счет")
        print("11. Смена рабочей директории")
        print("12. Выход")

        choice = input("Выберите пункт меню: ")

        if choice == "1":
            cf()
        elif choice == "2":
            dfof()
        elif choice == "3":
            cfof()
        elif choice == "4":
            vdc()
        elif choice == "5":
            vofof(choice)
        elif choice == "6":
            vofof(choice)
        elif choice == "7":
            view_operating_system_info()
        elif choice == "8":
            view_program_creator()
        elif choice == "9":
            play_quiz()
        elif choice == "10":
            bank_account()
        elif choice == "11":
            change_working_directory()
        elif choice == "12":
            exit_program()
        else:
            print("Неверный выбор. Попробуйте еще раз.")


if __name__ == "__main__":
    main()
