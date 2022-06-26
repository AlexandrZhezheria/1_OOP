"""
Создайте класс, описывающий книгу. Он должен содержать информацию об авторе, названии, годе издания и жанре.
Создайте несколько разных книг.
Определите для него операции проверки на равенство и неравенство, методы __repr__ и __str__.
"""

class Book:

    def __init__(self, book_author, book_name, book_year, book_genre):
        self.book_author = book_author
        self.book_name = book_name
        self.book_year = book_year
        self.book_genre = book_genre

    def __repr__(self):
        return f"author: {self.book_author} name: {self.book_name} year: {self.book_year} genre: {self.book_genre}"

    def __str__(self):
        return f"author: {self.book_author} name: {self.book_name} year: {self.book_year} genre: {self.book_genre}"


book1 = Book("Jack London", "White Fang", 1892, 122, "Classic")
book2 = Book("Jack Jordan", "Yellow Fang", 1992, 5, "Comedy")
book3 = Book("Jack London", "White Fang", 1998, 4, "Classic")
book4 = Book("Victor Gugo", "Les Miserables", 1843, 67, "Classic")

print book1
print(book1.__str__())

# s = str(p)
# print(s)
#
# print(p.__repr__())
# print(type(p.__repr__()))
# print(repr(p))
