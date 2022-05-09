fruits = []
try:
    for _ in range(0,10):
        fruit = input('Enter the name of te fruits: ')
        if fruit in fruits:
            raise ValueError(' This fruit is already here')
        fruits.append(fruit)

except ValueError as error:
    print(error)

print(fruits)

