from json import load, dump

books = []
try:
    with open('books.json') as file:
        books = load(file)

except FileNotFoundError:
    books = []

choice = input('Available commands [p]rint / [a]dd: ')

if choice == 'p':
    for book in books:
        print(f"- Author: {book['author']}, Tytle: {book['title']}, Pages: {book['pages']}")
elif choice == 'a':
    author = input('Name and surname of the author: ')
    title = input("Book's title: ")
    pages = input('Number of pages: ')

    books.append(
        {
            'author': author,
            'title': title,
            'pages': pages
        }
    )

    with open('books.json', 'w') as file:
        dump(books, file)

