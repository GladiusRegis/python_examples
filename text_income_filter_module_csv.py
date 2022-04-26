from csv import reader, writer
# https://docs.python.org/3/libraty/csv.html
# csv modules documentation

result = []
with open('transactions.csv', encoding='utf8') as input_file:
    content = reader(input_file, delimiter=',')
    next(content)

    #  for line in input_file:
        #  print(line.strip())
    for line in content:
        #  print(line)
        created_at, description, value = line

        if int(value) > 0:
            result.append(line)


with open('income.csv', 'w', encoding='utf8', newline='') as output_file:
    content = writer(output_file, delimiter=',')
    for line in result:
        content.writerow(line)

