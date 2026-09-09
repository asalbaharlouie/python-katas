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


def test_primes_up_to():
    assert primes_up_to(10) == [2, 3, 5, 7]


test_primes_up_to()


def test_primes_up_to_no_primes():
    assert primes_up_to(1) == []


test_primes_up_to_no_primes()


def test_primes_up_to_one_primes():
    assert primes_up_to(2) == []


test_primes_up_to_one_primes()


def test_primes_up_to_zero():
    assert primes_up_to(0) == []


test_primes_up_to_zero()

print(primes_up_to(20))
