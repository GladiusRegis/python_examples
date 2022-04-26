result = []
with open('transactions.csv', 'r', encoding='utf8') as input_file:
    next(input_file)
    for line in input_file:
        line_as_list = line.strip().split(',')
        #print(line_as_list)
        create_at, description, value = line_as_list
        if int(value) > 0:
            result.append(line)

#  print(result)

with open('income.csv', 'w', encoding='utf8') as output_file:
    output_file.writelines(result)
