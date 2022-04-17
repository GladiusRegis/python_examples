def get_brutto(netto, vat):
    return netto + netto * vat


values = [
    (100, 0.23),
    (50, 0.05)
]

for value in values:
    print(get_brutto(*value))

