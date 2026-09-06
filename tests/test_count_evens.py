def count_evens(nums):
    count = 0
    for i in nums:
        if i % 2 == 0:
            count += 1
    return count

def test_count_evens():
    assert count_evens([1, 2, 3, 4, 5, 6, 7]) == 3

test_count_evens()

print(count_evens([2, 5, 8, 11, 19, 22, 24, 28]))