def is_prime(number):

    prime = True
    if int(number) in [0, 1]:
        prime = False

    else:
        for div in range(2, int(int(number) ** 0.5) + 1):
            if int(number) % 2 == 0:
                prime = False
                break
    return prime


print(is_prime(input('Check that the integer is prime: ')))

