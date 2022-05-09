# while True:
#     try:
#         value = int(input('Enter number: '))
#         if not value % 5 == 0:
#             raise Exception('The number is not divisible by 5')
#
#         print(value)
#     except Exception as e:
#         print(e)


try:
    while True:
        value = int(input('Enter number: '))
        if not value % 5 == 0:
            raise Exception('The number is not divisible by 5')

        print(value)
except Exception as e:
    print(e)
