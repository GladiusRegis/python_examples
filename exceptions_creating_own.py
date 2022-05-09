class ValueToSmall(Exception):
    pass


class ValueToBig(Exception):
    pass


try:
    value = int(int('Enter number'))
    if value < 10:
        raise ValueToSmall()
    if value > 20:
        raise ValueToBig()

    print(value)
except (ValueToBig, ValueToBig) as error:
    print(error)
