def fizzbuzz(nums):
    res = []
    for num in nums:
        if num % 15 == 0:
            res.append("FizzBuzz")
        elif num % 3 == 0:
            res.append("Fizz")
        elif num % 5 == 0:
            res.append("Buzz")
        else:
            res.append(num)

    return res

def test_fizzbuzz():
    assert fizzbuzz([1, 2, 3, 4, 5, 9, 15]) == [1, 2, "Fizz", 4, "Buzz", "Fizz", "FizzBuzz"]

test_fizzbuzz()

print(fizzbuzz([1, 3, 5, 7, 8, 10, 21, 32]))