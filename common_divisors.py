def find_divisors(number):
   divisors = set()
   for divisor in range(2, number + 1)
       if number % divisor == 0:
           divisors.add(divisor)
   return divisors


test1 = calculate_common_divisor(3, 6)
print(test1)

test2 = calculate_common_divisor(3, 6, 4)
print(test2)

test3 = calculate_common_divisor(16, 8)
print(test3)



