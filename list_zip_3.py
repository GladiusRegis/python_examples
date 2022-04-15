def get_sum(list1: list, list2: list) -> list:
    # total = []
    # for a, b in zip(list1, list2):
    #     total.append(a + b)
    #
    # return total
    return [a + b for a, b in zip(list1, list2)]


list_one = [2, 4, 6]
list_two = [8, 6, 4]

print(get_sum(list_one, list_two))

