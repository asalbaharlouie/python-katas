def count_evens(nums):
    count = 0
    for i in nums:
        if i % 2 == 0:
            count += 1
    return count

print(count_evens([2, 5, 8, 11, 19, 22, 24, 28]))