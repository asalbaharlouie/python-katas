def my_list(MyList):
    total = 0
    for i in MyList:
        total += i
    return total

def test_my_list():
    assert my_list([1, 4, 5]) == 10

test_my_list()

def test_my_list_empty_list():
    assert my_list([]) == 0

test_my_list_empty_list()

print(my_list([2, 10, 8]))