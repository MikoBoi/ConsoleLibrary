class Book:

    def __init__(self, id, title, author, year, status="В наличии"):
        self.id = id
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def to_json(self):
        """Преобразование объекта книги в словарь для сохранения в JSON формате"""
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "status": self.status
        }

    @staticmethod
    def from_json(data):
        """Вывод объектов книги"""
        return Book(data["id"], data["title"], data["author"], data["year"], data["status"])