from json import load, dump

print("""Home library""")
finish = False
while finish is not True:
    menu = input("""Available commands:
                     - [p]rint
                     - [a]dd
                     - exit - other key
                             :""")

    with open('library.json', 'r') as data:
        books = load(data)

    if menu == 'p':
        print(f'Name of library: {books["title"]}')
        for book in books["books"]:
            print(f' - {book["author"]} - {book["title"]} - {book["pages"]}')

    elif menu == 'a':
        author = input('author: ')
        title = input('title: ')
        pages = input('pages: ')

        with open('library.json', 'w') as data:
            books['books'].append({
                'id': len(books["books"]) + 1,
                'author': author,
                'pages': pages
            })
        dump(books, data)

    else:
        finish = True
