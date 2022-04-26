value_sum = 0
with open('income.csv', 'r', encoding='utf8') as input_file:
    for line in input_file:
        line_arr = line.strip().split(',')
        created_at, title, value = line_arr
        value_sum += int(value)

print(value_sum)
