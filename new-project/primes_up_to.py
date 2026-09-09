def primes_up_to(n):
    primes_number = []
    for number in range(2, n):
        find_divisor = False
        for divisor in range(2, number - 1):
            if number % divisor == 0:
                find_divisor = True
        if not find_divisor:
            primes_number.append(number)

    return primes_number


print(primes_up_to(20))
