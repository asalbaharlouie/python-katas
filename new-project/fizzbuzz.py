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

print(fizzbuzz([1, 3, 5, 7, 8, 10, 21, 32]))