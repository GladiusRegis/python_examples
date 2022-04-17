def total_salary(base, calculate_extra):
    return base + calculate_extra(base)


def calculate_ten_percent(amount):
    return 0.1 * amount


def calculate_zero(amount):
    return 0
# nawet jeśli będziemy dawać 0 to i tak tę funkcję musimy zadeklarować


print(total_salary(1000, calculate_ten_percent))

print(total_salary(1000, calculate_zero))
