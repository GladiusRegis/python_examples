from datetime import datetime


class Book:
    def __init__(self, title, kind, authors, summary, description, rating):
        self.title = title
        self.kind = kind
        self.author = authors
        self.summary = summary
        self.description = description
        self.rating = rating


class Author:
    def __init__(self, first_name, last_name, date_of_birth):
        self.first_name = first_name
        self.last_name = last_name
        self.date_birth = date_of_birth


bonifacy = Author('Bonifacy', 'Smith', datetime(1910, 10, 10))
john = Author('John', 'Smith', datetime(1905, 5, 15))
book = Book(
    'Sample title',
    'Detective story',
    [bonifacy, john],
    'Summary',
    'Description',
    10.5
)
