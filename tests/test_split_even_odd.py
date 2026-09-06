def split_even_odd(numbers):
    even_list = []
    odd_list = []
    for num in numbers:
        if num % 2 == 0:
            even_list.append(num)
        else:
            odd_list.append(num)

    return even_list, odd_list 

def test_split_even_odd():
    assert split_even_odd([1, 2, 3, 4]) == ([2, 4], [1, 3])

test_split_even_odd()

def test_split_even_odd_when_even():
    assert split_even_odd([2, 4, 6]) == ([2, 4, 6], [])

test_split_even_odd_when_even()

def test_split_even_odd_when_odd():
    assert split_even_odd([5, 7]) == ([], [5, 7])

test_split_even_odd_when_odd()

def test_split_even_odd_when_empty():
    assert split_even_odd([]) == ([], [])

test_split_even_odd_when_empty()

print(split_even_odd([10, 32, 12, 87, 91, 10, 29, 54]))