from Classes.Book import *
import os
import json

class Library:

    def __init__(self):
        self.data_file = "./data.json"
        self.books = self.load_file()

    def load_file(self):
        '''Загружаем JSON файл'''

        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, "r", encoding="utf-8") as file:
                    data = json.load(file)
                    return [Book.from_json(book) for book in data]

        # В случае если файл пустой, добавляем скобочки и сохряняем.
        except:
            with open(self.data_file, "w", encoding="utf-8") as file:
                json.dump([], file)

    def save_file(self):
        '''Сохраняем изменения в JSON файл'''

        with open(self.data_file, 'w', encoding='utf-8') as file:
            json.dump([book.to_json() for book in self.books], file, ensure_ascii=False, indent=4)



    def add_book(self, title, author, year):
        '''Добавление книги'''

        # Данный блок кода необходим для автоинкремента ID.
        max_id = 0
        for book in self.books:
            if book.id > max_id:
                max_id = book.id
        id = max_id + 1

        new_book = Book(id, title, author, year)
        self.books.append(new_book)
        self.save_file()
        print(f"Книга \"{title}\" добавлена!")



    def remove_book(self, id):
        '''Удаление книги'''

        for book in self.books:
            if book.id == id and book.status == "Запись удалена":
                return print("Записи больше не существует")

            elif book.id == id:
                print(f"\nЗапись:\t\t\t{book.title},\t{book.author},\t{book.year} год\t\tСтатус: {book.status}")

                # Данный блок для предотвращения или совершения действия
                while True:
                    print("Вы точно хотите удалить данную запись?")
                    i = input("0. Нет\t1. Да\t: ")
                    if i == "0":
                        return print("Понял, возвращаемся в меню.")
                    elif i == "1":
                        # self.books.remove(book)

                        # Для того чтобы автоинкремент не присваивал себе ID последней по списку записи, если она была удалена.
                        book.title = None
                        book.author = None
                        book.year = None
                        book.status = "Запись удалена"
                        self.save_file()
                        return print(f"Книга с ID-{id} удалена.")
                    else:
                        print("Выберите из предложенных вариантов!\n")
                        continue
        return print(f"Книга с ID-{id} не найдена.")



    def search(self, search, found=False):
        '''Поиск книг(и)'''

        print("\nНайденные книги соответствующие запросу:")
        for book in self.books:
            if book.status != "Запись удалена":
                if search in book.title.lower() or search in book.author.lower() or search == str(book.year):
                    found = True
                    print(f"\tID: {book.id},\n\tНазвание: {book.title},\n\tАвтор: {book.author},\n\tГод: {book.year},\n\tСтатус: {book.status}")
                    print("\t----------------------------------------------")

        # Выводим если переменная found = False. Если поиск не увенчался успехом.
        if found != True:
            return print("\tКниги соответствующие запросу не найдены!")

        input("\nНажмите Enter чтобы вернуться ")



    def show_books(self):
        '''Отображение книг'''

        # Если еще не добавлено книг.
        if not self.books:
            return print("Нет книг в библиотеке.")

        # Если есть книги
        print("Книги:")
        for book in self.books:
            if book.status != "Запись удалена":
                print(f"\tID: {book.id},\n\tНазвание: {book.title},\n\tАвтор: {book.author},\n\tГод: {book.year},\n\tСтатус: {book.status}")
                print("\t----------------------------------------------")

        input("\nНажмите Enter чтобы вернуться ")



    def change_status(self, id):
        '''Изменение статуса книги'''

        for book in self.books:
            if book.id == id and book.status == "Запись удалена":
                return print("Записи больше не существует")

            elif book.id == id:
                print(f"\nЗапись:\t\t\t{book.title},\t{book.author},\t{book.year} год\t\tСтатус: {book.status}")
                print("Выберите доступный статус: ")
                if book.status == "В наличии":
                    enter = input("\t0. Выдана\t: ")
                    new_status = "Выдана" if enter == "0" else None
                else:
                    enter = input("\t0. В наличии\t: ")
                    new_status = "В наличии" if enter == "0" else None

                #Если выбрана несуществующая опция.
                if new_status is None:
                    print("Данной опций нет!\n")
                    return self.change_status(id)

                #Данный блок для предотвращения или совершения действия
                while True:
                    print("Вы точно хотите изменить статус данной записи?")
                    i = input("0. Нет\t1. Да\t: ")
                    if i == "0":
                        return print("Понял, возвращаемся в меню.")
                    elif i == "1":
                        book.status = new_status
                        self.save_file()
                        return print(f"Статус книги с ID-{id} изменена.")
                    else:
                        print("Выберите из предложенных вариантов!\n")
                        continue

        return print(f"Книга с ID-{id} не найдена.")