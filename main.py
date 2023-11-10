from create_folder import create_folder as cf
from delete_file_or_folder import delete_file_or_folder as dfof
from copy_file_or_folder import copy_file_or_folder as cfof
from view_and_save_directory_contents import view_directory_contents as vdc
from view_and_save_directory_contents import save_directory_contents as sdc
from view_only_folders_or_files import view_only_folders_or_files as vofof
from seven_functions import *

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
        print("5. Cохранение содержимого рабочей директории в файл")
        print("6. Посмотреть только папки")
        print("7. Посмотреть только файлы")
        print("8. Просмотр информации об операционной системе")
        print("9. Создатель программы")
        print("10. Играть в викторину")
        print("11. Мой банковский счет")
        print("12. Смена рабочей директории")
        print("13. Выход")

        choice = input("Выберите пункт меню: ")

        if choice == "1":
            print(cf())
        elif choice == "2":
            print(dfof())
        elif choice == "3":
            print(cfof())
        elif choice == "4":
            print(vdc())
        elif choice == "5":
            print(sdc())
        elif choice == "6":
            print(vofof(choice))
        elif choice == "7":
            print(vofof(choice))
        elif choice == "8":
            print(view_operating_system_info())
        elif choice == "9":
            print(view_program_creator())
        elif choice == "10":
            play_quiz()
        elif choice == "11":
            bank_account()
        elif choice == "12":
            print(change_working_directory())
        elif choice == "13":
            exit_program()
        else:
            print("Неверный выбор. Попробуйте еще раз.")


if __name__ == "__main__":
    main()
