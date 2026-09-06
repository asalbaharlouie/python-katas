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

def test_factorial_iterative():
    assert factorial_iterative(5) == 120

test_factorial_iterative()

def test_factorial_iterative_zero():
    assert factorial_iterative(0) == 1

test_factorial_iterative_zero()

print(factorial_iterative(4))
print(factorial_recursive(4))