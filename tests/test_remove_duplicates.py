def remove_duplicates(items):
    seen_list = []
    seen_set = set()
    for item in items:
        if item not in seen_set:
            seen_list.append(item)
            seen_set.add(item)

    return seen_list 

def test_remove_duplicates():
    assert remove_duplicates([1, 2, 3, 2, 1]) == [1, 2, 3]

test_remove_duplicates()

def test_remove_duplicates_empty():
    assert remove_duplicates([]) == [] 

test_remove_duplicates_empty()

def test_remove_duplicates_all_same():
    assert remove_duplicates([5, 5, 5, 5]) == [5]  

test_remove_duplicates_all_same()

def test_remove_duplicates_strings():
    assert remove_duplicates(["a", "b", "a", "c"]) == ["a","b","c",]

test_remove_duplicates_strings()

print(remove_duplicates([1, 2, 4, 4, 3, 1, 2, 2]))