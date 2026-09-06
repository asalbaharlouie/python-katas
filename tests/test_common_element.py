def common_elements(list1, list2):
    my_set1 = set(list1) 
    my_set2 = set(list2)
    res = set()
#داره رو تک تک آیتم های my_set1 راه میره 
    for item in my_set1:
#پی اینجا آیتم های my_set2 رو باهاش مقایسه میکنیم
        if item in my_set2: 
            res.add(item)
    return res

def test_common_elements():
    assert common_elements([1, 2, 3], [2, 3, 4]) == {2, 3}

test_common_elements()

def test_commom_elements_when_one_list_empty():
    assert common_elements([1, 3, 6], []) == {1, 3, 6}

test_commom_elements_when_one_list_empty()

def test_commom_elements_when_both_empty():
    assert common_elements([], []) == {}

test_commom_elements_when_both_empty()

def test_common_elements_when_no_common():
    assert common_elements([1, 2, 3], [4, 5, 6]) == {}

test_common_elements_when_no_common()

def test_common_elements_when_identical_lists():
    assert common_elements([1, 2, 3], [1, 2, 3]) == {1, 2, 3}

test_common_elements_when_identical_lists()

def test_common_elements_with_duplicates():
    assert common_elements([1, 1, 2, 3], [1, 3, 5, 7, 7]) == {1, 3}

test_common_elements_with_duplicates()

print(common_elements([1, 9, 21, 11], [11, 21, 1, 1, 8, 3]))