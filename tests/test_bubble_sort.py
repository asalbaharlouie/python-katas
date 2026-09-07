def bubble_sort(numbers):
    for i in range(len(numbers)):
        for j in range(len(numbers)-1):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    
    return numbers

def test_bubble_sort():
    assert bubble_sort([5, 2, 9, 1]) == [1, 2, 5, 9]

test_bubble_sort()

def test_bubble_sort_duplicates():
    assert bubble_sort([3, 1, 9, 7 , 7]) == [1, 3, 7, 7, 9]

test_bubble_sort_duplicates()

def test_bubble_sort_empty():
    assert bubble_sort([]) == []

test_bubble_sort_empty()

def test_bubble_sort_one_member():
    assert bubble_sort([2]) == [2]

test_bubble_sort_one_member()

def test_bubble_sort_sorted_list():
    assert bubble_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

test_bubble_sort_sorted_list()

print(bubble_sort([2, 4, 6, 7, 3, 3, 20]))