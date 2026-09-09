def find_max(MyList):
    max_num = MyList[0]
    for i in MyList:
        if i > max_num:
            max_num = i
    return max_num


def test_find_max():
    assert find_max([1, 5, 11]) == 11


test_find_max()

print(find_max([-3, -29, -0.5, -4]))
