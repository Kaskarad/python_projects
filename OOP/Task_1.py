class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True

    def __str__(self):
        return f"Название: {self.title}, Автор: {self.author}, ISBN: {self.isbn}, Доступна: {self.available}"


class User:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.available:
            book.available = False
            self.borrowed_books.append(book)
            print(f"{self.name} взял книгу '{book.title}'")
        else:
            print(f"Книга '{book.title}' недоступна")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.available = True
            self.borrowed_books.remove(book)
            print(f"{self.name} вернул книгу '{book.title}'")
        else:
            print(f"{self.name} не может вернуть книгу '{book.title}', так как она не была взята")

    def __str__(self):
        borrowed_titles = [book.title for book in self.borrowed_books]
        return f"Имя пользователя: {self.name}, Взятые книги: {borrowed_titles}"


class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Книга '{book.title}' добавлена в библиотеку")

    def add_user(self, user):
        self.users.append(user)
        print(f"Пользователь '{user.name}' добавлен в библиотеку")

    def list_available_books(self):
        available_books = [book.title for book in self.books if book.available]
        return available_books

    def list_borrowed_books(self):
        borrowed_books = [book.title for book in self.books if not book.available]
        return borrowed_books


# Пример использования:

# Создаем книги
book1 = Book("1984", "Джордж Оруэлл", "123456789")
book2 = Book("Мастер и Маргарита", "Михаил Булгаков", "987654321")

# Создаем пользователей
user1 = User("Иван Иванов")
user2 = User("Мария Петрова")

# Создаем библиотеку и добавляем в нее книги и пользователей
library = Library()
library.add_book(book1)
library.add_book(book2)
library.add_user(user1)
library.add_user(user2)

# Пользователь берет книгу
user1.borrow_book(book1)
print(user1)  # Имя пользователя: Иван Иванов, Взятые книги: ['1984']

# Список доступных книг в библиотеке
print(library.list_available_books())  # ['Мастер и Маргарита']

# Пользователь возвращает книгу
user1.return_book(book1)
print(user1)  # Имя пользователя: Иван Иванов, Взятые книги: []

# Список доступных книг в библиотеке
print(library.list_available_books())  # ['1984', 'Мастер и Маргарита']