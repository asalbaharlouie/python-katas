def factorial_iterative(n):
    number = 1
    for num in range(1, n+1):
        number *= num

    return number

def factorial_recursive(n):
    if n == 0:
        return 1 
    else:
        return n * factorial_recursive(n-1)

print(factorial_iterative(4))
print(factorial_recursive(4))