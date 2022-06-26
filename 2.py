"""
Создайте класс, описывающий отзыв к книге. Добавьте в класс книги поле – список отзывов.
Сделайте так, что при выводе книги на экран при помощи функции print также будут выводиться отзывы к ней.
"""


class Book:

    def __init__(self, author, name, year_of_publishing, genre):
        self.author = author
        self.name = name
        self.year_of_publishing = year_of_publishing
        self.genre = genre
        self.reviews = []

    def add_review(self, user, review):
        self.reviews.append(Review(user, review))

    def info_book(self):
        for info in (self.author, self.name, self.year_of_publishing, self.genre):
            print(info)
        for review in self.reviews:
            print(review)


class Review:

    def __init__(self, user, review):
        self.user = user
        self.review = review

    def __str__(self):
        return f'пользователь - {self.user}\n отзыв - {self.review}'


book_1 = Book("orwell", "1984", 2015, "fiction")
book_1.add_review("Olexandr", "Прочитал на одном дыхании!")
book_1.add_review("Iryna", "Отлично!")
book_1.info_book()
