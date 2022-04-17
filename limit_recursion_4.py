def limit_recursion_check(n):
    print(n)
    limit_recursion_check(n+1)


limit_recursion_check(0)
