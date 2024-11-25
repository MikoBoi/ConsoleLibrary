from Classes.Library import *
from time import sleep

lib = Library()

def cases():
    '''Кейсы'''

    try:
        while True:
            print("\n")
            print("--------------------------------------------------")
            print("Добро пожаловать в консольную библиотеку!")
            print("\nДоступные операции: ")
            print("\t1. Добавить книгу")
            print("\t2. Удалить книгу")
            print("\t3. Найти книгу")
            print("\t4. Показать все книги")
            print("\t5. Изменить статус книги")
            print("\t0. Выход")

            case = input("\nВыберите действие: ")

            print("--------------------------------------------------")

            if case == "1":         # Добавить книгу.
                title = input("Введите название книги: ")
                author = input("Введите автора книги: ")
                while True:         # Некая система валидации.
                    try:
                        year = int(input("Введите год издания: "))
                        if 700 <= year <= 2025:
                            lib.add_book(title, author, year)
                            break
                        else:       # Если формат введенных данных неправильный.
                            print("Пожалуйста, укажите год между 700 и 2025.\n")
                            continue
                    except:         # В случае ввода символов вместо чисел.
                        print("Неправильный формат года! Введите числовое значение (например, 1999 или 777).\n")
                        continue

            elif case == "2":       # Удалить книгу.
                while True:         # Некая система валидации.
                    try:
                        id = int(input("Введите ID книги, которую хотите удалить: "))
                        lib.remove_book(id)
                        break
                    except:         # В случае ввода символов.
                        print("Неправильный формат ID!\n")
                        continue

            elif case == "3":       # Поиск.
                search = input("\nУкажите название\автора\года издания книги, которую хотите найти: ")

                # Переводим строку к нижнему регистру.
                lib.search(search.lower())

            elif case == "4":       # Отображение всех книг.
                lib.show_books()

            elif case == "5":       # Изменение статуса книги.
                while True:         # Некая система валидации.
                    try:
                        id = int(input("Введите ID книги, статус которой вы хотите изменить: "))
                        lib.change_status(id)
                        break
                    except:         # В случае ввода символов.
                        print("Неправильный формат ID!\n")
                        continue

            elif case == "0":       # Выход.
                print("Заглядывайте!")
                break

            else:                   # Если любое другое значение.
                print("Нет такой операций в нашей системе!")

            sleep(3)

    # Выводим если консольку закрыли с помощью Ctrl+C.
    except: print("\n\n\nВнимание: Внезапное отключение!!!")