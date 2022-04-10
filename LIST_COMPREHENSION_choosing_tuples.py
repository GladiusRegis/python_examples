tuples = [
    (1,),  # (1,) the item must be followed by a COMMA !!! OTHERWISE, IT IS NOT TUPLE
    (2, 3),
    (3, 4),
    (4, 3, 4),
    (1, 2, 3, 4),
    (2, 3, 4, 5),
    (2, 2, 2),
    (1, 1, 1, 5, 4, 3, 4)
]

result = [sum(item) if len(item) % 2 == 0 else round(sum(item) / len(item), 2) for item in tuples if 1 < len(item) < 6]
print(result)
