from csv import reader, writer
# https://docs.python.org/3/libraty/csv.html
# csv modules documentation

result = []
with open('transactions.csv', encoding='utf8') as input_file:
    content = reader(input_file, delimiter=',')  # delimiter - separator
    next(content)  # przejście do kolejnego wiersza - nie potrzebujemy nagłówka
    for line in content:  # teraz iterujemy content a nie input_file
        # print(line.strip())  # (1)
        #  print(line)  # (2)
        # są przecinki można zrobić split, ale lepiej skorzystać z biblioteki csv
        created_at, description, value = line  # rozpakowanie
        # print(int(value))  # (3)
        if int(value) > 0:
            result.append(line)
            # można i tu zapisywać za każdym razem do pliku za pomocą a
            # with open(.... , 'a')
            #      write.
            # za każdym razem trzeba otwierać i zamykać plik
            # można zrobić z użyciem generatora i zwracać każdą pojedyńcząl linę

with open('income.csv', 'w', encoding='utf8', newline='') as output_file:  # newline - aby nie było pustej linie
    content = writer(output_file, delimiter=',')
    for line in result:
        content.writerow(line)

